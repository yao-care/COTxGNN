"""依原收集規則補收 INVIMA CUM 現行清單有、證據包沒收的本藥 expediente（2026-11-25 第六輪，用戶決定；全程不用 AI）。

問題：證據包的許可是 src/cotxgnn/collectors/cofda.py 收的（2026-11-05 依成分重建，scripts/rebuild_licenses_by_ingredient.py）：
藥名／DrugBank ID → data/processed/drug_mapping.csv 裡同一個 ID 的 expediente → data/raw/co_fda_drugs.json（2026-03 的 CUM 有效資料集）
的那幾列；排除 fields.yaml 的 withdrawn_statuses，依 expediente 去重、單方在前，最多存 20 筆，total_matches＝不重複 expediente 數。
2026-03 之後才出現在 CUM 有效／暫時未上市狀態的 expediente 不在 drug_mapping、也不在 co_fda_drugs.json，永遠收不進來。

收集規則確認（每個證據包第一次跑時）：照同一支收集器、同一份 drug_mapping.csv 與 co_fda_drugs.json 重算一次，
存下的紀錄（號碼與順序）與 total_matches 都要跟證據包完全相同，才記 tfda.collection_rule；當時算進 total_matches、
因 20 筆上限沒存的 expediente 回填 tfda.records_not_stored（避免之後重複計數）。重算不出來的證據包整個不補、列進報告（停損，不推定）。
已記收集規則的證據包，之後每次確認 total_matches＝records＋records_not_stored 的不重複號碼數，不符也停損。

補收（只加不刪、可重複執行）：data/raw/invima_cum_estado.json（license_adapter.fetch() 的四個 CUM 資料集，2026-11-25 起帶成分）裡
- 現行狀態對到 valid（Vigente、En tramite renov）或 not_marketed（Temp. no comerc 等，法律上仍有效）的 expediente
  （原收集器只收有效資料集、排除 withdrawn_statuses；用戶 2026-11-25 決定只補這兩類），
- 不在 co_fda_drugs.json（新 expediente），
- 每個 principioactivo 照同一份 drug_mapping.csv 的「原始成分字串 → DrugBank ID」對照（成功的列）；drug_mapping 沒見過的字串
  用 run_kg_prediction.py 同一支 map_fda_drugs_to_drugbank 對（drug_mapping 裡對照失敗的字串照舊算對不到），
- 對到的 DrugBank ID 跟證據包 tfda.drugbank_ids 有交集（複方照原規則逐成分歸屬），證據包還沒有（records、records_not_stored）的就補。
records 未滿 20 筆存進 records（單方在前、再依號碼），滿了只記號碼在 records_not_stored；都算進 total_matches。
紀錄欄位照收集器 _format（產品名、成分、ATC 描述、劑型、持有人取現行清單），另記 license_status、source（清單與日期、規則）與 added（補收日）。
EXCLUDE：看起來不是原規則會收的（不是本藥、獸用等），每筆附理由；目前空。

用法（repo 根目錄）：python3 scripts/add_current_licenses.py [--download] [--dry-run] [--report out.tsv]
--download：先以 license_adapter.fetch() 下載現行清單（成功且通過 validate 才覆寫 data/raw/invima_cum_estado.json）。
每週排程（.github/workflows/license-refresh.yml）在 license_refresh 前以 --download 跑（失敗不擋排程）。
"""
import collections
import csv
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))
import license_adapter as ad  # noqa: E402

BUNDLES = ROOT / "data/bundles"
RAW = ROOT / "data" / ad.RAW_FILE
BASE_LIST = ROOT / "data/raw/co_fda_drugs.json"
MAPPING = ROOT / "data/processed/drug_mapping.csv"
CAP = 20
KEEP = ("valid", "not_marketed")
RULE = "cofda.py（2026-11-05 依成分重建；drug_mapping.csv＋co_fda_drugs.json 2026-03）"
EXCLUDE = {}  # {expediente: 理由}
SPLIT = re.compile(r"[,;+/&]|&&| and | y | e | und | et ")
csv.field_size_limit(10**9)


def _collector_all(col, drug, dbid):
    """照 cofda.py search() 重算：回傳（存下的 20 筆號碼、全部不重複號碼依同一排序、drugbank_ids）。"""
    col._prepare()
    ids = col._drugbank_ids(drug)
    if dbid:
        ids.add(str(dbid).upper())
    recs = []
    for db in sorted(ids):
        for lic in sorted(col.db_to_lic.get(db, ())):
            recs.extend(col.by_license.get(lic, []))
    if not recs:
        recs = col._text_match(drug)
    act = [r for r in recs if not col._is_withdrawn(r)]
    d = col._format(act, ids)
    ing_f = col.fm.get("ingredients")
    seen, order = set(), []
    for r in sorted(act, key=lambda r: len(SPLIT.split(str(r.get(ing_f, "") or "")))):
        k = str(r.get(col.fm.get("license_id"), "") or "").strip()
        if k and k not in seen:
            seen.add(k)
            order.append(k)
    return [x["license_id"] for x in d.get("records") or []], order, d.get("total_matches", 0)


def load_raw():
    raw = json.loads(RAW.read_text(encoding="utf-8"))
    if not any(r.get("principioactivo") for r in raw):
        sys.exit("invima_cum_estado.json 沒有成分欄（2026-11-25 前的格式）；先以 --download 下載")
    idx = ad.status_index(raw)
    det = {}
    for r in raw:  # 取現行狀態那個資料集的那一列
        e = r["expediente"]
        if e in idx and r["estado"] == idx[e][0] and e not in det:
            det[e] = r
    for r in raw:
        det.setdefault(r["expediente"], r)
    return idx, det


def ingredient_map(strings):
    by, failed = collections.defaultdict(set), set()
    with open(MAPPING, encoding="utf-8-sig") as f:
        for x in csv.DictReader(f):
            k = x["original_ingredient"].strip().lower()
            if x["mapping_success"] == "True" and x.get("drugbank_id"):
                by[k].add(x["drugbank_id"].strip().upper())
            else:
                failed.add(k)
    need = sorted({s for s in strings if s.strip().lower() not in by and s.strip().lower() not in failed})
    if need:
        import pandas as pd
        from cotxgnn.mapping.drugbank_mapper import map_fda_drugs_to_drugbank
        m = map_fda_drugs_to_drugbank(pd.DataFrame([{"lic": str(i), "brand": "", "ing": s} for i, s in enumerate(need)]),
                                      field_mapping={"license_id": "lic", "brand_name": "brand", "ingredients": "ing"})
        for _, x in m.iterrows():
            if isinstance(x.get("drugbank_id"), str) and x["drugbank_id"]:
                by[need[int(x["license_id"])].strip().lower()].add(x["drugbank_id"].strip().upper())
    return by


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    if "--download" in argv:
        new = ad.fetch()
        old = json.loads(RAW.read_text(encoding="utf-8")) if RAW.exists() else []
        p = ad.validate(new, old)
        if p:
            sys.exit("下載的清單沒通過檢查，不補收：" + "；".join(p))
        if not dry:
            RAW.write_text(json.dumps(new, ensure_ascii=False, indent=1), encoding="utf-8")
    idx, det = load_raw()
    edition = datetime.date.fromtimestamp(RAW.stat().st_mtime).isoformat()
    base = {str(x.get("expediente")) for x in json.loads(BASE_LIST.read_text(encoding="utf-8"))}
    cand = sorted(e for e, (_, c) in idx.items() if c in KEEP and e not in base and e not in EXCLUDE)
    by = ingredient_map({p for e in cand for p in det[e].get("principioactivo") or []})
    dbs = {e: set().union(*[by.get(p.strip().lower(), set()) for p in det[e].get("principioactivo") or []] or [set()]) for e in cand}
    cand = [e for e in cand if dbs[e]]
    ncomp = {e: len(det[e].get("principioactivo") or []) or 1 for e in cand}

    from cotxgnn.collectors.cofda import LocalFDACollector
    col = LocalFDACollector()
    today = datetime.date.today().isoformat()
    rows, held = [], []
    nb = nrec = nstore = nrule = nfill = 0
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        b = json.loads(f.read_text(encoding="utf-8"))
        t = b.get("tfda") or {}
        recs = list(t.get("records") or [])
        have = [str(r.get("license_id")) for r in recs]
        not_stored = [str(x) for x in t.get("records_not_stored") or []]
        rule = t.get("collection_rule")
        changed = False
        if not rule:
            drug = b.get("drug") or {}
            stored, order, tm = _collector_all(col, drug.get("inn") or page.replace("_", " "), drug.get("drugbank_id"))
            if stored != have or tm != (t.get("total_matches") or 0) or len(order) != tm:
                held.append(f"{page}\t原收集規則重算不出：存 {len(have)}／重算 {len(stored)}，total_matches {t.get('total_matches')}／重算 {tm}")
                continue
            rule, not_stored, changed = RULE, order[CAP:], True
            nrule += 1
            nfill += bool(not_stored)
        else:
            if len(set(have) | set(not_stored)) != (t.get("total_matches") or 0):
                held.append(f"{page}\ttotal_matches {t.get('total_matches')} ≠ records＋records_not_stored {len(set(have) | set(not_stored))}")
                continue
        ids = {x.upper() for x in t.get("drugbank_ids") or []}
        known = set(have) | set(not_stored)
        hit = sorted((e for e in cand if dbs[e] & ids and e not in known), key=lambda e: (ncomp[e] > 1, e))
        added = []
        for e in hit:
            r = det[e]
            text, cls = idx[e]
            ing = " + ".join(r.get("principioactivo") or [])
            src = f"INVIMA CUM {r.get('dataset')} {edition}（{RULE}：成分對 drug_mapping 的 DrugBank ID，新 expediente 依成分補收）"
            rows.append(f"{page}\t{e}\t{text}\t{ing}\t{r.get('producto', '')}\t{'records' if len(recs) < CAP else 'not_stored'}")
            if len(recs) < CAP:
                recs.append({"license_id": e, "brand_name_zh": r.get("producto", ""), "brand_name_en": ing, "ingredients": ing,
                             "indication": r.get("descripcionatc", ""), "dosage_form": " | ".join(r.get("formafarmaceutica") or []),
                             "manufacturer": r.get("titular", ""), "license_holder": r.get("titular", ""), "approval_date": "",
                             "expiry_date": "", "status": text, "license_status": cls, "source": src, "added": today})
                nstore += 1
            else:
                not_stored.append(e)
            added.append(e)
        if not added and not changed:
            continue
        nb += bool(added)
        nrec += len(added)
        t2 = dict(t, records=recs, total_matches=(t.get("total_matches") or 0) + len(added), found=bool(recs) or bool(t.get("found")),
                  collection_rule=rule)
        if not_stored:
            t2["records_not_stored"] = not_stored
        if not dry:
            b["tfda"] = t2
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\texpediente\testado\tprincipioactivo\tproducto\tstored\n" + "\n".join(rows) + "\n", encoding="utf-8")
        Path(rep).with_suffix(".held.tsv").write_text("\n".join(held) + "\n", encoding="utf-8")
    print(f"候選新 expediente（valid／not_marketed、對得到 DrugBank）{len(cand)} 個")
    print(f"記下收集規則：{nrule} 個證據包（回填 records_not_stored {nfill} 個）；停損 {len(held)} 個")
    print(f"補收 {nb} 個證據包 {nrec} 筆（存進 records {nstore}、只算張數 {nrec - nstore}）" + ("（試跑，未寫入）" if dry else ""))


if __name__ == "__main__":
    main(sys.argv[1:])
