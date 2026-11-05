"""CO 依成分（expediente 去重）重建證據包的許可證紀錄（2026-11-05，用戶核准；全程不用 AI；做法比照 ZaTxGNN）。

原本的許可證紀錄來自 src/cotxgnn/collectors/cofda.py：INVIMA CUM 每個包裝、每個成分各一列，收集器先截 20 列再算，
同一 expediente 佔滿 20 列（amlodipine 有 128 張，只收到 RACORVAL 2 張 Temp. no comerc，頁面就寫成「核准未上市」），
total_matches 又是列數（28），不是張數。收集器已改成先依 expediente 去重再截 20 筆、total_matches＝不重複 expediente 數。

本支用修好的收集器（同一份 data/raw/co_fda_drugs.json、data/processed/drug_mapping.csv）重跑每個證據包的許可證查詢，
再套 data/raw/invima_cum_estado.json 的現行狀態（scripts/license_adapter.py，與每週排程相同的對應）。
只換證據包的 tfda.records／total_matches／found，其他欄位不動。
停損：原本收錄、新結果卻沒有的 expediente 超過一半 → 對應可能改變，不改、列進報告。
用法（repo 根目錄）：python3 scripts/rebuild_licenses_by_ingredient.py [--dry-run] [--report out.tsv] [頁 ...]
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
import license_adapter as ad  # noqa: E402
from cotxgnn.collectors.cofda import LocalFDACollector  # noqa: E402

BUNDLES = ROOT / "data/bundles"


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    only = [a for a in argv if not a.startswith("--") and a != rep]
    idx = ad.status_index(json.loads((ROOT / "data" / ad.RAW_FILE).read_text(encoding="utf-8")))
    col = LocalFDACollector()
    rows, held, changed = [], [], 0
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        if only and page not in only:
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        reg = b.get("tfda") or {}
        drug = b.get("drug") or {}
        res = col.search(drug.get("inn") or page.replace("_", " "), drugbank_id=drug.get("drugbank_id"))
        if not res.success:
            held.append(f"{page}\t查詢失敗：{res.error_message}")
            continue
        new = res.data
        for r in new.get("records") or []:
            k = ad.record_id(r)
            if k in idx:
                ad.update(r, idx[k])
        old_ids = {ad.record_id(r) for r in reg.get("records") or []}
        new_ids = {ad.record_id(r) for r in new.get("records") or []}
        lost = old_ids - new_ids
        if old_ids and len(lost) * 2 > len(old_ids) and int(new.get("total_matches") or 0) <= len(new_ids):
            held.append(f"{page}\t原有 {len(old_ids)} 張、{len(lost)} 張不在新結果：{','.join(sorted(lost)[:5])}")
            continue
        nreg = dict(reg, found=new.get("found", False), records=new.get("records") or [], total_matches=new.get("total_matches", 0))
        if nreg == reg:
            continue
        rows.append(f"{page}\t{len(old_ids)}\t{reg.get('total_matches')}\t{len(new_ids)}\t{nreg['total_matches']}")
        changed += 1
        if not dry:
            b["tfda"] = nreg
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\told_unique\told_total_matches\tnew_records\tnew_total_matches\n" + "\n".join(rows) + "\n", encoding="utf-8")
        Path(rep).with_suffix(".held.tsv").write_text("\n".join(held) + "\n", encoding="utf-8")
    print(f"重建 {changed} 個證據包（停損擋下 {len(held)} 個）")


if __name__ == "__main__":
    main(sys.argv[1:])
