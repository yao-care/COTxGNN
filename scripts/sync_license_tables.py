"""藥物頁「## Información de Mercado en Colombia」段落的許可證表改由程式依證據包產生（2026-11-24，用戶決定；全程不用 AI）。

為什麼：市場段落原本是 AI 寫的自由格式表（品名欄寫「(vigente)」、狀態欄寫「Temp. no comerc - Vigente」…），INVIMA 資料每週變，
表上的狀態與列數就跟事實矛盾，checker 擋下整頁、開 issue 要人處理。改成程式表後，每週排程（license_adapter.sync_tables）自動重排。
做法比照 SgTxGNN／UkTxGNN／UsTxGNN 的同名程式：
- 段落裡第一張表（不論原欄位）換成「| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |」
  （本站 112 頁原本的寫法；原表第四欄「Indicación Aprobada」放的其實是 CUM 的 descripcionatc（ATC 分類說明），不是適應症，照實改名）。
  欄位全取證據包 tfda.records（INVIMA CUM 原文）：expediente、producto、formafarmaceutica、descripcionatc、estadoregistro（排程更新後的現行狀態）。
- 排序：vigentes（Vigente、En tramite renov）→ 暫時未上市（Temp. no comerc - Vigente 等，法律上仍有效）→ 已失效（Vencido、Cancelado…）；
  同一類照證據包原順序（收集器已把單一成分排在前面）。
- 列數：原表列數與 min(5, 總數) 取大（最多 20）；段落裡有 AI 寫的「列出幾筆」說明句（se muestran／se listan／la tabla muestra／
  los N principales…）時照原表列數，免得說明句跟表對不上。重排時以頁面上現有程式表的列數為準，所以每週重排列數不變。
- 表下一句程式說明（SHOW）：列數＝總數時「Se muestran los N registros…」，較少時「Se muestran N de M…」，證據包只收了部分紀錄
  （total_matches 大於收錄筆數）時寫「Se muestran N de al menos K…」（K＝收錄筆數，同概覽表張數列的「al menos」）。
- 證據包沒有任何紀錄時拿掉表，改一句 NONE_LINE。段落裡沒有表的頁在標題下補程式區塊。表以外的 AI 文字不動
  （正文張數由 scripts/rewrite_license_counts.py 依事實層改寫）。
程式區塊標記：程式產生的表（連同 SHOW 句，或 NONE_LINE）前後各一行「<!-- licenses:begin -->」「<!-- licenses:end -->」，
讓查核紀錄、刪句工具與 gate 分得出哪些字是程式寫的；gate（src/cotxgnn/regulatory/site.py 的 program_block_problems）
依 snapshots/co_licenses.json.gz 檢查程式區塊＝快照重算的結果。
誰會跑：每週許可證排程（scripts/license_adapter.py 的 sync_tables）、依成分重建（scripts/license_rebuild_run.py）、
sync_notes_to_docs.py 重寫整頁時以 carry_block 移植舊頁程式區塊。
用法（repo 根目錄，先還原 data/）：python3 scripts/sync_license_tables.py [--dry-run] [--check] [頁 ...]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC_RE = re.compile(r"^## Informaci[oó]n de Mercado en Colombia\s*$")
HEAD = ["| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |",
        "|---------|------|------|------|------|"]
SRC = "INVIMA, Código Único de Medicamentos"
NONE_LINE = (f"No se encontraron registros sanitarios de este principio activo en los datos del {SRC} (datos.gov.co), "
             "usados para este informe.")
SHOW_ALL1 = f"Se muestra el único registro sanitario de este principio activo en los datos del {SRC}."
SHOW_ALL = "Se muestran los {m} registros sanitarios de este principio activo en los datos del " + SRC + "; primero los vigentes."
SHOW_SOME = "Se muestran {n} de {m} registros sanitarios de este principio activo en los datos del " + SRC + "; primero los vigentes."
SHOW_PART = ("Se muestran {n} de al menos {m} registros sanitarios de este principio activo en los datos del " + SRC +
             "; primero los vigentes. Los datos de este informe solo incluyen parte de los registros.")
SHOW_RX = re.compile(r"^Se muestra(n)? (el único|los \d+|\d+ de (al menos )?\d+) registros? sanitarios? de este principio activo en los datos del "
                     r"INVIMA, Código Único de Medicamentos")
# tools/txgnn/.claude/known_use_pages_20261022.py 在它產生的表下寫的程式句（舊程式表的部分紀錄提示）：程式表的 SHOW 句已涵蓋，拿掉
PART_NOTE = "Los datos solo contienen parte de los registros; la lista puede estar incompleta."
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
MAX_ROWS = 20
# AI 寫的「表上列了幾筆」說明句：有這種句子時程式表照原表列數（不擴到 5 列），免得句子跟表對不上
DISPLAY_RX = re.compile(r"\bse (muestran|listan|incluyen|presentan)\b|\bla tabla (muestra|incluye|lista)|\blos \d+ principales\b|"
                        r"\b(primer[oa]s|principales) \d+\b|\bfilas\b|\bno se muestra", re.I)
RANK = {"valid": 0, "not_marketed": 1, "unknown": 2, "cancelled": 3}
VALID_TEXT = {"vigente", "en tramite renov"}


def cls(rec):
    ls = rec.get("license_status")
    if ls:
        return ls
    return "valid" if str(rec.get("status") or "").strip().lower() in VALID_TEXT else "unknown"


def cell(x, n=80):
    t = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    return t if len(t) <= n else t[:n - 1].rstrip() + "…"


def table_rows(recs):
    seen, out = set(), []
    for i, r in sorted(enumerate(recs), key=lambda x: (RANK.get(cls(x[1]), 2), x[0])):
        k = str(r.get("license_id") or "").strip()
        if not k or k in seen:
            continue
        seen.add(k)
        out.append(f"| {k} | {cell(r.get('brand_name_zh') or r.get('brand_name_en'), 90) or 'Sin dato'} | "
                   f"{cell(r.get('dosage_form'), 60) or 'Sin dato'} | {cell(r.get('indication'), 70) or 'Sin dato'} | "
                   f"{cell(r.get('status'), 50) or 'Sin dato'} |")
    return out


def show_line(n, total, partial, k):
    if partial:
        return SHOW_PART.format(n=n, m=k)
    if n >= total:
        return SHOW_ALL1 if total == 1 else SHOW_ALL.format(m=total)
    return SHOW_SOME.format(n=n, m=total)


def counts(tf):
    recs = tf.get("records") or []
    rows = table_rows(recs)
    tm = int(tf.get("total_matches") or 0)
    partial = tm > len(rows)
    return rows, (tm if partial else len(rows)), partial


def block_for(tf, n):
    """程式區塊的內容（不含標記）：n 列的表＋SHOW 句；沒有任何紀錄時是 NONE_LINE 一句"""
    rows, total, partial = counts(tf)
    if not rows:
        return [NONE_LINE]
    n = max(1, min(n, len(rows), MAX_ROWS))
    return HEAD + rows[:n] + ["", show_line(n, total, partial, len(rows))]


def rows_of(tf, fc=None):
    """快照用：(最多 20 列可列的列, 總數)；另由 build_license_snapshot 存 partial／listed（gate 重算 SHOW 句用）"""
    rows, total, partial = counts(tf)
    return rows[:MAX_ROWS], total


def snap_extra(tf):
    rows, total, partial = counts(tf)
    return {"partial": partial, "listed": len(rows)}


def strip_marks(lines):
    return [l for l in lines if l.strip() not in (BEGIN, END)]


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


def _bounds(lines):
    a = next((i for i, l in enumerate(lines) if SEC_RE.match(l)), None)
    if a is None:
        return None, None
    a += 1
    return a, next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))


def _review_mask(lines):
    """查核框（<!-- review:begin … review:end -->）內的行號：找表、判斷說明句時不算"""
    m, inside = set(), None
    for i, l in enumerate(lines):
        s = l.strip()
        if inside is None and s.startswith("<!-- review:begin "):
            inside = s.split()[2]
        if inside is not None:
            m.add(i)
            if s == f"<!-- review:end {inside} -->":
                inside = None
    return m


def _target_rows(lines, a, b, x, y, nrows_avail):
    """程式表列數：原表資料列數 r0；段落有『列了幾筆』說明句時照 r0，否則 max(r0, min(5, 可列筆數))；上限 20"""
    r0 = max(0, (y - x + 1) - 2)
    mask = _review_mask(lines)
    disp = any(DISPLAY_RX.search(lines[k]) for k in range(a, b) if k not in mask and not lines[k].startswith("|")
               and not SHOW_RX.match(lines[k].strip()))
    n = r0 if (disp and r0) else max(r0, min(5, nrows_avail))
    return max(1, min(MAX_ROWS, n))


def _is_prog(l):
    s = l.strip()
    return bool(SHOW_RX.match(s)) or s in (NONE_LINE, PART_NOTE)


def process(text, tf):
    """回傳新內容；沒有變就回 None"""
    lines = strip_marks(text.split("\n"))
    a, b = _bounds(lines)
    if a is None:
        t2 = add_section("\n".join(lines), tf)
        return t2 if t2 and t2 != text else None
    mask = _review_mask(lines)
    tb = [k for k in range(a, b) if lines[k].startswith("|") and k not in mask]
    rows, total, partial = counts(tf)
    if not tb:
        blk = block_for(tf, min(5, len(rows)))
        k = a
        while k < b and not lines[k].strip():
            k += 1
        # 已有 NONE_LINE（舊版）就換掉，不重複
        rest = [l for l in lines[a:b] if not _is_prog(l)]
        while rest and not rest[0].strip():
            rest.pop(0)
        out = lines[:a] + [""] + wrap(blk) + [""] + rest + lines[b:]
    else:
        x = y = tb[0]
        while y + 1 < b and lines[y + 1].startswith("|"):
            y += 1
        n = _target_rows(lines, a, b, x, y, len(rows))
        rest = [l for l in lines[y + 1:b] if not _is_prog(l)]
        while rest and not rest[0].strip():
            rest.pop(0)
        head = lines[:x]
        while head and not head[-1].strip():
            head.pop()
        # 原表前後若有程式 SHOW／NONE 句（重排時）一併拿掉
        head = [l for i, l in enumerate(head) if i < a or not _is_prog(l)]
        out = head + [""] + wrap(block_for(tf, n)) + [""] + rest + lines[b:]
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    return t2 if t2 != text else None


# 2026-11-24 第三輪（用戶決定，比照 JpTxGNN 第二輪）：公開頁沒有「## Información de Mercado en Colombia」段落、但證據包有
# 衛生登記紀錄的，補一個段落放程式表（min(5, 可列筆數) 列＋SHOW 句）。位置：「## Consideraciones de Seguridad」之前（預測頁的固定順序）；
# 沒有就「## Conclusión y Próximos Pasos」之前；再沒有（已知用途頁）就「## Descargo de responsabilidad」之前。
# noindex 頁與證據包沒有紀錄的頁不補。
SEC = "## Información de Mercado en Colombia"
ADD_BEFORE = ("Consideraciones de Seguridad", "Conclusión y Próximos Pasos", "Conclusion y Proximos Pasos", "Descargo de responsabilidad")


def add_section(text, tf):
    fm = text.split("---", 2)[1] if text.startswith("---") else ""
    rows = counts(tf)[0]
    if re.search(r"^noindex:\s*true", fm, re.M) or not rows:
        return None
    lines = text.split("\n")
    heads = {m.group(1): i for i, l in enumerate(lines) for m in [re.match(r"^## (.+?)\s*$", l)] if m}
    at = next((heads[h] for h in ADD_BEFORE if h in heads), None)
    if at is None:
        return None
    sec = [SEC, ""] + wrap(block_for(tf, min(5, len(rows)))) + [""]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines[:at] + sec + lines[at:]))


def block_lines(text):
    """頁面上程式區塊的內容行（不含標記與空行）；沒有區塊回 None"""
    lines = text.split("\n")
    if BEGIN not in lines or END not in lines:
        return None
    i, j = lines.index(BEGIN), lines.index(END)
    return [x for x in lines[i + 1:j] if x.strip()]


def expected_block(entry, n):
    """gate 用：依快照（rows、total、partial、listed）重算 n 列的程式區塊（不含空行）"""
    rows = entry.get("rows") or []
    if not rows:
        return [NONE_LINE]
    n = max(1, min(n, entry.get("listed") or len(rows), MAX_ROWS))
    return HEAD + rows[:n] + [show_line(n, entry.get("total") or len(rows), bool(entry.get("partial")),
                                        entry.get("listed") or len(rows))]


def carry_block(old_text, new_text):
    """sync_notes_to_docs.py 重寫整頁時用：舊頁的程式區塊移植到新頁的市場段落，取代新頁模型寫的第一張表；
    新頁段落沒有表時接在標題下。舊頁沒有程式區塊就原樣回傳新頁。"""
    old = old_text.replace("\r\n", "\n").split("\n")
    if BEGIN not in old or END not in old:
        return new_text
    blk = old[old.index(BEGIN):old.index(END) + 1]
    lines = strip_marks(new_text.split("\n"))
    a, b = _bounds(lines)
    if a is None:
        return new_text
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        out = lines[:a] + [""] + blk + [""] + lines[a:]
    else:
        x = y = tb[0]
        while y + 1 < b and lines[y + 1].startswith("|"):
            y += 1
        rest = [l for l in lines[y + 1:b] if not SHOW_RX.match(l.strip())]
        out = lines[:x] + blk + [""] + rest + lines[b:]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def _bundle(stem):
    for key in (stem, stem.replace("-", "_"), stem.replace("_", "-")):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return f
    return None


def run(only=None, dry=False):
    """回傳 [(頁, 欄位, 前值, 後值)]（每週排程摘要用）"""
    if not (ROOT / "data/bundles").is_dir() or not any((ROOT / "data/bundles").glob("*/drug_bundle.json")):
        raise SystemExit("找不到 data/bundles（先還原 data/）；讀不到證據包不改頁")  # 交付前驗證：讀不到資料就停
    ch = []
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only is not None and page.stem not in only and page.stem.replace("-", "_") not in only:
            continue
        bf = _bundle(page.stem)
        if bf is None:
            continue
        raw = page.read_bytes().decode("utf-8")
        if "layout: id_redirect" in raw[:3000] or 'http-equiv="refresh"' in raw[:3000]:
            continue
        crlf = "\r\n" in raw[:500]
        t = raw.replace("\r\n", "\n")
        tf = json.loads(bf.read_text(encoding="utf-8")).get("tfda") or {}
        new = process(t, tf)
        if new is None:
            continue
        before, after = block_lines(t), block_lines(new)
        ch.append((page.stem, "Información de Mercado en Colombia（程式許可證表）",
                   f"{len([x for x in before or [] if x.startswith('| ') and not x.startswith(HEAD[0])])} 列" if before else "AI 表／無表",
                   f"{len([x for x in after or [] if x.startswith('| ') and not x.startswith(HEAD[0])])} 列"))
        if not dry:
            page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return ch


def main(argv):
    only = {a for a in argv if not a.startswith("--")} or None
    ch = run(only, dry="--dry-run" in argv or "--check" in argv)
    if "--check" in argv:
        print(f"程式許可證表：{'✗' if ch else '✓'} 待重排 {len(ch)} 頁")
        sys.exit(1 if ch else 0)
    print(f"程式許可證表：改 {len(ch)} 頁")


if __name__ == "__main__":
    main(sys.argv[1:])
