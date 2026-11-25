"""量測：INVIMA CUM 現行清單（data/raw/invima_cum_estado.json，2026-11-25 起帶成分）有、證據包沒收的本藥 expediente（只量、不改；2026-11-25 用戶第五輪決定）。

規則照原收集器（src/cotxgnn/collectors/cofda.py）：expediente 的每個 principioactivo → DrugBank ID（同一成分字串在 data/processed/drug_mapping.csv
已有對照就沿用，沒有就照 run_kg_prediction.py 同一支 map_fda_drugs_to_drugbank 對照），跟證據包 tfda.drugbank_ids 有交集、不在證據包
records／excluded_records 的算漏收。原收集器只收 2026-03 有效資料集（data/raw/co_fda_drugs.json）、排除 fields.yaml 的 withdrawn_statuses，
所以這裡只算現行狀態對到 valid（Vigente、En tramite renov）或 not_marketed（Temp. no comerc 等，法律上仍有效）的 expediente；過期、撤銷等不算。
「新」＝不在 co_fda_drugs.json 的 expediente。不放寬。
用法：python3 scripts/measure_cum_new_items.py [--out 檔.json]
"""
import argparse, collections, csv, glob, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src")); sys.path.insert(0, str(ROOT / "scripts"))


def page_kind(slug):
    p = ROOT / "docs/_drugs" / f"{slug}.md"
    if not p.exists():
        return "nopage"
    fm = p.read_text(encoding="utf-8").split("---")[1]
    return "redirect" if "id_redirect" in fm else ("noindex" if re.search(r"^noindex:\s*true", fm, re.M) else "public")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out"); a = ap.parse_args()
    import pandas as pd
    import license_adapter as ad
    from cotxgnn.mapping.drugbank_mapper import map_fda_drugs_to_drugbank
    D = ROOT / "data"
    raw = json.loads((D / ad.RAW_FILE).read_text(encoding="utf-8"))
    if not any(r.get("principioactivo") for r in raw):
        sys.exit("invima_cum_estado.json 沒有成分欄（2026-11-25 前的格式）；先跑每週排程或 license_adapter.fetch()")
    idx = ad.status_index(raw)
    ing = collections.defaultdict(list)
    for r in raw:
        for p in r.get("principioactivo") or []:
            if p not in ing[r["expediente"]]:
                ing[r["expediente"]].append(p)
    base = set()
    with open(D / "raw/co_fda_drugs.json", encoding="utf-8") as f:
        base = {str(x.get("expediente")) for x in json.load(f)}
    by_orig = collections.defaultdict(set)
    for x in csv.DictReader(open(D / "processed/drug_mapping.csv", encoding="utf-8-sig")):
        if x["mapping_success"] == "True" and x.get("drugbank_id"):
            by_orig[x["original_ingredient"].strip().lower()].add(x["drugbank_id"].upper())
    new = sorted(e for e, (_, c) in idx.items() if e not in base and c in ("valid", "not_marketed"))
    need = [{"lic": e, "brand": "", "ing": p} for e in new for p in ing.get(e, []) if p.strip().lower() not in by_orig]
    mapped = collections.defaultdict(set)
    if need:
        m = map_fda_drugs_to_drugbank(pd.DataFrame(need), field_mapping={"license_id": "lic", "brand_name": "brand", "ingredients": "ing"})
        for _, x in m.iterrows():
            if isinstance(x.get("drugbank_id"), str) and x["drugbank_id"]:
                mapped[str(x["license_id"])].add(x["drugbank_id"].upper())
    db = {e: set().union(*[by_orig.get(p.strip().lower(), set()) for p in ing.get(e, [])] or [set()]) | mapped.get(e, set()) for e in new}
    prod = {r["expediente"]: r.get("producto", "") for r in raw}
    per, tot = [], collections.Counter()
    for bf in sorted(glob.glob(str(D / "bundles/*/drug_bundle.json"))):
        slug = Path(bf).parent.name
        t = json.loads(Path(bf).read_text(encoding="utf-8")).get("tfda") or {}
        ids = {x.upper() for x in t.get("drugbank_ids") or []}
        have = {str(r.get("license_id")) for r in (t.get("records") or []) + (t.get("excluded_records") or [])}
        hit = [e for e in new if db[e] & ids and e not in have]
        if not hit:
            continue
        kind, partial = page_kind(slug), (t.get("total_matches") or 0) > len(t.get("records") or [])
        nv = sum(1 for e in hit if idx[e][1] == "valid")
        per.append({"slug": slug, "page": kind, "partial": partial, "n": len(hit), "valid": nv, "not_marketed": len(hit) - nv,
                    "records": len(t.get("records") or []), "total_matches": t.get("total_matches"),
                    "items": [[e, idx[e][0], " + ".join(ing.get(e, [])), prod.get(e, "")] for e in hit]})
        tot["bundles"] += 1; tot["items"] += len(hit); tot["items_valid"] += nv; tot[f"bundles_{kind}"] += 1
        tot["bundles_partial" if partial else "bundles_complete"] += 1
    cls = collections.Counter(c for _, c in idx.values())
    s = {"current_expedientes": len(idx), "by_class": dict(cls), "base": len(base), "new_valid_or_not_marketed": len(new),
         "new_mapped": sum(1 for v in db.values() if v), "new_in_some_bundle": len({i for p in per for i, *_ in p["items"]}), **tot}
    print(json.dumps(s, ensure_ascii=False))
    if a.out:
        Path(a.out).write_text(json.dumps({"summary": s, "bundles": per}, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
