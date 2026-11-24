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
| 許可證 | `scripts/sync_license_tables.py`（程式表前後有 `<!-- licenses:begin/end -->` 標記，2026-11-24 起）、`snapshots/co_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/cotxgnn/regulatory/licenses.py` | 快照存本藥號碼、事實層與程式表列；gate 依快照驗程式區塊、市場段落表格的號碼歸屬、狀態列與張數列、表格列狀態 |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依成分重建刪句後（`scripts/license_rebuild_run.py` 有的話會自動跑）或依 git 前後版本，把正文刪改轉成 correct 紀錄 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證；本站證據包有 INVIMA 適應症文字，2026-11-12 可比對 627 頁、5 頁列入待查 |
| gate | `scripts/check_seo_docs.py` 第 17–20、22 項 | 紀錄都已套用、許可證＝快照（含程式表）、頁首＝本站規則算出的等級、撤回預測沒有對外發布、正文張數＝程式改寫結果 |

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

## 市場段落許可證表與正文張數改由程式維護（2026-11-24）

用戶 2026-11-24 決定（30 站逐站做，本站是第一波試點、A＋B 都做）：每週許可證排程只改概覽表狀態列／張數列，AI 寫的自由格式許可證表（品名欄「(vigente)」、
狀態欄「Temp. no comerc - Vigente」）與正文寫死的張數會跟每週變的 INVIMA CUM 矛盾，checker 擋頁、開 issue（例 11-23 排程擋下 5 頁、靠 co-row-20261124-* 人工更正）。
- A. `scripts/sync_license_tables.py`：市場段落（Información de Mercado en Colombia）的第一張表換成程式依證據包產生的表
  「| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |」（欄位全取 INVIMA CUM 原文：expediente、producto、formafarmaceutica、
  descripcionatc、estadoregistro；原表第四欄「Indicación Aprobada」放的其實是 descripcionatc，照實改名）；排序 vigentes→暫時未上市→已失效；
  列數＝原表列數與 min(5, 總數) 取大（上限 20），段落裡有 AI「列了幾筆」說明句時照原表列數；表下程式句「Se muestran N de M registros sanitarios…」
  （部分紀錄寫「de al menos K」）；沒有紀錄時寫 NONE_LINE；段落沒有表的 7 頁在標題下補程式區塊；known_use_pages 的舊部分紀錄提示句（PART_NOTE）拿掉。
  前後 `<!-- licenses:begin/end -->`；gate 由 `site.program_block_problems` 依快照（rows、total、partial、listed）重算比對（列數依頁面，1～20）。
  接進：每週排程（`scripts/license_adapter.py` 的 sync_tables＋PAGE_NOTE，3b 自我檢查認得程式句）、依成分重建（`scripts/license_rebuild_run.py`）、
  `sync_notes_to_docs.py` 整頁重寫時 carry_block 移植舊程式區塊、`build_license_snapshot.py` 存程式表列（rows_of／snap_extra）。
- B. `scripts/rewrite_license_counts.py`＋`src/cotxgnn/regulatory/count_prose.py`（照 KrTxGNN／MyTxGNN 2026-11-12 的同名程式移植，句型改西班牙文）：依快照事實層改寫
  句型明確的「N registros (sanitarios) vigentes／N licencias válidas／N registros (… cancelados)」；本站「vigente」＝有效或有效＋暫時未上市都算對（INVIMA Temp. no comerc
  法律上仍有效），要改時改成有效數；有保留（al menos、parcial、datos compilados…）、相對數、劑型或廠商子集、顯示筆數、部分紀錄頁不改，同一行有判斷不了的整行不動。
  `apply_drug_reviews.py`（非 --check）結尾、`build_license_snapshot.py` 寫完快照後（`--no-rewrite` 不跑；license_rebuild_run 轉紀錄前用）都會跑；gate 第 22 項擋「再跑一次會變」。
  不再顯示的查核紀錄（superseded、resolved_*、withdrawn）不保護原句。
- 2026-11-24 套用：公開藥物頁 622 頁中 613 頁的 AI 表換掉（表頭 472 頁「…| Indicación Aprobada |」、112 頁加 Estado、15 頁 known_use_pages 舊程式表等）、
  7 頁補程式區塊，2 頁（etanercept、imipenem）沒有市場段落不動；連 noindex 共 623 頁。錨在舊表列上的 5 筆 co-row-20261124-*（11-23 排程擋頁的人工更正）標 superseded。
  co-lic-20261112-* 純張數更正 47 筆中，非部分紀錄頁、句子由 B 管得到的 32 筆標 resolved_by_program（張數改由程式維護；其中 dacarbazine 4→3、oxaliplatin 8→7、
  tenofovir_disoproxil 16→15 是快照更新後已過期的數字，由 B 改寫）；部分紀錄頁 14 筆、naphazoline 1 筆（句子有劑型子集）維持。
  獨立偵測找到 3 頁市場段落說「Ningún registro (está／se encuentra) vigente」而事實全部有效（miglustat 2/2、spironolactone 11/11、tetrabenazine 2/2；10 月誤判註銷的殘句，
  checker X_LOCAL es 漏抓），以 co-lic-20261124-*-1 刪除。描述舊 AI 表的說明句、數詞或廠商子集寫死的張數 19 句（例 sunitinib「Los cuatro registros pertenecen a…」共 20 張、
  dexketoprofen「Ambos registros…」共 9 張、「Fabricante: …」只講舊表那一張）判斷不了，列進待查清單（source：市場段落換成程式許可證表後…）。
  AI 寫的「La lista de registros puede ser parcial.」43 頁照舊（保留語，不是錯的事實）。
- 已知限制：每週排程 3c checker 在 4b（套紀錄、建快照→B 改寫正文）之前跑，這週事實變動造成正文矛盾、且 checker 認得的句子仍會先擋頁；B 改寫的是下一步。

## 同一 DrugBank ID 的重複公開頁改轉址（2026-11-19）

用戶 2026-11-19 決定（照 ARTxGNN 同日做法）：公開藥物頁同一 DrugBank ID（front matter drugbank_id，沒有的用證據包 drug.drugbank_id 與 dbXXXXX 轉址頁推斷）、預測相同的，留一頁、另一頁改轉址（layout: id_redirect、permalink 不變、sitemap: false、search_exclude、nav_exclude）。
20 組 21 頁，各組許可證號完全相同；保留順序：查核紀錄數→字數（差 5% 內算平手）→西文 INN 名，保留頁等級不低於被轉址頁。
轉址：leuprolide_acetato→leuprolide、baclofeno→baclofen、azitromicina→azithromycin、amlodipino→amlodipine、beclometasona、beclometasona_dipropionato→beclomethasone_dipropionate、ampicilina→ampicillin、alopurinol→allopurinol、lansoprazole→lansoprazol（平手）、lenalidomida→lenalidomide、lamotrigina→lamotrigine、lamivudina→lamivudine、acetato_de_hidrocortisona→hydrocortisone、azatioprina→azathioprine、amoxicillin→amoxicilina（平手）、atazanavir_sulfato→atazanavir、atorvastatin→atorvastatina、leflunomida→leflunomide、aripiprazol→aripiprazole、acetato_de_indacaterol→indacaterol、aceclofenac→aceclofenaco。
dbXXXXX 轉址頁原本指到被轉址頁的（db00448、db01060、db01076、db06736）改成直接指保留頁，沒有轉址鏈；db00381 仍指 amlodipine（保留頁）。llms.txt／llms-full.txt 的範例藥 Atorvastatin 換成 Atorvastatina。
被轉址頁的查核紀錄（leuprolide_acetato、amlodipino、alopurinol、lenalidomida 各 1 筆，全是 resolved_by_regeneration）留在 drug_reviews.json 當歷史（apply_drug_reviews 跳過轉址頁）。
公開藥物頁 643→622；FHIR 的 MK 以 DrugBank ID 命名，不變（608）；衍生檔、hreflang 照重產。

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 494 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `co-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：本站語言（español）的出處句＋節錄的忠實翻譯（標明「非官方翻譯」）＋英文原文（照引、為準）＋DailyMed 連結、仿單版本、取用日期（用戶 2026-11-19 決定「當地語言摘要＋英文原文」）。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 翻譯：節錄的翻譯是 AI 輔助的忠實翻譯（不增不減，藥名、基因與受體符號、數字、「[…]」照原文），2026-11-19 批次產生，存在紀錄 sources 的 translation（translation_lang、translation_note 註明非官方、英文原文為準）；頁面上同時列英文原文。`--translations <檔>` 讀翻譯、`--need <檔>` 列出還沒翻的節錄（這些頁那次不寫紀錄，gate 會擋，翻好再跑）。
- 2026-11-19 結果：442 頁寫入紀錄（美國仿單 404、ChEMBL 38），52 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）；ChEMBL 譯文（詞組清單）後補句號 38 筆；同 id 重發，前版 replacement 存 history。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；偵測漏抓的「不可得」句補 2 筆紀錄、1 頁列待查；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「Indicación original: No consta en los datos locales」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：INVIMA 衛生登記（暫時未上市另列）。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：dronabinol「Indicación original: No consta en los datos locales」→「En Colombia, registros sanitarios del INVIMA: 4 (vigentes: 0; además, temporalmente no comercializados: 4)」；2026-11-19 改了 2 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site COTxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。

## 第二輪：舊表說明句、保留語與紀錄裡的寫死張數（2026-11-24）

用戶 2026-11-24 第二輪決定（第一輪列進待查的事逐句處理、紀錄說明不再寫死張數）：
- 待查清單 19 句（描述舊 AI 表的說明句、數詞或廠商子集寫死的張數）逐句對照事實層（2026-11-23）與證據包：更正文字本身是舊表說明的 1105 紀錄同 id 重發（dexketoprofen、lorazepam「Ambos registros pertenecen a …」、bupivacaine、ketamine、terazosin「Fabricante: …」、mometasone「El sexto registro (DIFENZ®)」整句刪除；brigatinib「Ambos」→「Todos」，3 張皆 Takeda），
  其餘寫新紀錄 `co-lic-20261124b-*`（capecitabine、lovastatin、sertaconazole、fusidic_acid、naphazoline、mupirocin、sunitinib 整句刪；efavirenz「三個都是複方」不成立（20021554、20063470 是單方）刪；methylprednisolone「Ambos productos son de vía oral」刪（另有注射用粉劑）；cilastatin「Los tres」→「Todos」；fluorouracil、isotretinoin 表前引言改成不寫數字）。19 項標 resolved，附 record_ids。
- 劑型說法：市場段落全量掃描 19 句逐句對照證據包全部品項劑型；不成立的改寫：trimethoprim（1105 紀錄保留的「唯一劑型口服、沒有眼用」，證據包有注射液與 OQ-PLUS 眼用軟膏，同 id 重發刪除）、bisoprolol（另有 TABLETA）、desloratadine（7 張、錠劑與糖漿→實際含溶液、膠囊）、cabergoline、artemether（單數「Este registro」→複數）、fenofibrate（「Este producto es una combinación」→點名 PRAVAFEN®，另兩張單方）。其餘成立、保留。
- 市場段落 AI 保留語「La lista (de registros) puede ser parcial」等：程式表說明句已寫顯示幾張、共幾張（部分收錄頁另寫「solo incluyen parte de los registros」），所以市場段落裡的保留語句（約 85 頁）以紀錄刪除，同句裡跟事實不符的張數（cabazitaxel 5、ciprofibrate 4、fluoxetine、metoprolol、albendazole、dipyridamole 等）一併刪；amikacin「表由程式補上」句一併刪。另寫的獨立寬偵測又找到 lidocaine「3 registros disponibles」、montelukast「Fabricante: TECNOFAR」，同樣處理。剩下 25 句的張數／單一持有人說法逐句查過跟事實層一致，不改。
- 紀錄更正文字裡的張數：co-lic-20261112-* 與 co-lic-20261124-epinastine-1 的 replacement 改成不寫數字（「cuenta con registros sanitarios vigentes」等），note 改指向 Resumen rápido 與程式表，被點名的註冊號（artemether、octreotide、epinastine 的 19977977）保留；
  co-lic-20261105 的殘句（methotrexate「los dos y…」、methylphenidate「los cuatro y si…」）只留去掉錯誤前提的建議；glycine、cefalotin 的寫死張數拿掉；denosumab、lisinopril、midodrine、palivizumab、trifluoperazine、upadacitinib、ruxolitinib 保留句的「Ambos／Los tres registros」改「Todos los registros」（事實層查證仍成立）。
- 張數樣板：`src/cotxgnn/regulatory/site.py` 的 `_fig()` 原本寫死「El medicamento tiene N registros sanitarios (vigentes: V)」，改成不寫數字的一句；既有 775 筆紀錄說明同 id 重發（前版存 history，框的查核日期不變）。
- 合計：新紀錄 112 筆、同 id 重發 829 筆（含 2 筆改錨）；刪掉舊表說明句後 sync_license_tables 照一般規則（至少 5 列）重排 6 頁程式表（cefpodoxime、cholecalciferol、ciprofibrate、fluoxetine、lidocaine、metoprolol）。checker 前後 0、gate exit 0。
