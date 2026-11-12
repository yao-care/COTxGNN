# COTxGNN - Claude CLI 使用指引

本站（哥倫比亞，INVIMA）的維運規則。站群共用流程見母 repo yao-care/txgnn 的 CLAUDE.md；本檔只記本站自己的機制。

- 本專案結果僅供研究參考，不構成醫療建議
- 老藥新用候選需經過臨床驗證才能應用
- 所有網站頁面需包含 YMYL 免責聲明

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」「藥物頁許可證表與張數」兩節；
做法同 UsTxGNN，見 UsTxGNN/CLAUDE.md 同名一節）。規則與程式都在本 repo；頁面文字用西班牙文，依據是INVIMA CUM（Código Único de Medicamentos，datos.gov.co）。本站的在地設定集中在 `src/cotxgnn/regulatory/site.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、每頁查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/cotxgnn/regulatory/page_format.py`（規則在 site.py 的 HEADER_RULE） | 頁首＝Resumen rápido「Nivel de Evidencia」格的**第一個**等級（主預測）。2026-11-12 實測 611 頁有總覽等級，全部符合；整格取最高會有 3 頁不同 |
| 撤回預測 | `src/cotxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/co_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/cotxgnn/regulatory/licenses.py` | 快照存本藥號碼與事實層；gate 依快照驗市場段落表格的號碼歸屬、狀態列與張數列、表格列狀態（本站沒有程式產生的許可證表，所以沒有程式區塊標記） |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依成分重建刪句後（`scripts/license_rebuild_run.py` 有的話會自動跑）或依 git 前後版本，把正文刪改轉成 correct 紀錄 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證；本站證據包有 INVIMA 適應症文字，2026-11-12 可比對 627 頁、5 頁列入待查 |
| gate | `scripts/check_seo_docs.py` 第 17–20 項 | 紀錄都已套用、許可證＝快照、頁首＝本站規則算出的等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、license_rebuild_run.py、每週排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（排程與重建會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 依成分重建後直接刪掉的矛盾子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 896 筆紀錄（429 頁；其中 8 筆因報告在 11 月經 AI 重產、原句已不在頁面，標 resolved_by_regeneration）。
`scripts/sync_notes_to_docs.py` 依 notes 重寫整頁時，會重套紀錄（有程式許可證表的站也保留舊頁的程式區塊），notes 裡的舊錯句會被紀錄再更正一次。
2026-11-12 正文許可證張數對事實層掃描：62 頁 66 筆 correct 紀錄（`co-lic-20261112-*`）把 AI 正文裡依 10-31 前舊證據包寫的「N registros vigentes」等張數改成事實層（vigentes＝程式狀態列的有效張數；資料只收到 20 筆上限的頁寫「al menos N」）。正文數字＝有效＋暫時未上市（Temp. no comerc - Vigente，法律上仍有效）的不改；artemether、rivastigmine、octreotide 的「一／兩張註冊」2026-11-12 依事實層與證據包逐句改寫（`co-lic-20261112-{artemether,rivastigmine,octreotide}-1`：2、11、2 張；下文的單一產品說法查過仍成立），錨在 octreotide 那句的 co-lic-20261105-octreotide-2 改錨、前版存 history。
