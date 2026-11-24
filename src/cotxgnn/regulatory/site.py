"""本站（COTxGNN）查核機制的在地設定（2026-11-12 建）：頁面文字、資料來源、頁首規則、許可證格式、歷史刪改提交。

同目錄 page_format／licenses／withdrawn 與 scripts/apply_drug_reviews.py、build_license_snapshot.py、reviews_from_edits.py、
check_original_indications.py 都讀這裡；核心流程比照 TwTxGNN 與 UsTxGNN，只有這份是本站自己的寫法。
本站的市場資料是 INVIMA CUM（Código Único de Medicamentos，datos.gov.co；註冊狀態 Vigente／Vencido 等，號碼＝expediente），
頁面文字用西班牙文。市場段落的許可證表 2026-11-24 起由程式產生（scripts/sync_license_tables.py，前後有 licenses:begin／end 標記；
用戶 2026-11-24 決定，原本是報告寫的表），gate 依快照驗程式區塊（program_block_problems）。
"""
import importlib.util
import re
from pathlib import Path

SITE = "COTxGNN"
CODE = "co"
BUNDLE_KEY = "tfda"  # 證據包裡本站市場資料的鍵（收集器沿用的欄位名）

# ---------- 頁首等級（page_format） ----------
LEVEL_LABELS = ["Nivel de Evidencia", "Nivel de evidencia"]
HEADER_LABEL = r"Nivel de evidencia"
WITHDRAWN = r"Retirad[ao]"
# 頁首規則：2026-11-12 實測 611 頁有總覽等級，頁首全部＝格裡第一個等級（主預測）；整格取最高會有 3 頁不同
HEADER_RULE = "first"
DESC_LEVEL_RE = re.compile(r"nivel de evidencia (L[1-5]|N/A)\b(?![–-]L)", re.I)


def desc_level_text(level):
    return "solo usos conocidos" if level == "N/A" else f"nivel de evidencia {level}"


DISCLAIMER_RE = re.compile(r"^## Descargo de responsabilidad\b", re.M)

# ---------- 頁面文字（apply_drug_reviews） ----------
T = {
    "label": {"correct": "Corrección de revisión", "annotate": "Nota de revisión", "rereview": "Pendiente de nueva revisión",
              "rereview_result": "Resultado de la nueva revisión"},
    "action": {"correct": "Corregido", "annotate": "Nota añadida", "rereview": "Marcado para nueva revisión",
               "section": "Sección con fuente añadida", "rereview_result": "Nueva revisión completada",
               "header_level": "Nivel de evidencia del encabezado recalculado a partir del Resumen rápido",
               "description_level": "Nivel de evidencia de la descripción de la página igualado al del encabezado"},
    "verdict": {"maintain": "Mantenido", "downgrade": "Rebajado", "upgrade": "Elevado", "withdraw": "Retirado"},
    "log_head": "## Registro de revisión",
    "log_cols": "| Fecha de revisión | Elemento | Acción | Fuente |",
    "head": "> **{label} ({date})**: ",
    "originally": "Texto original: \"{claim}\"",
    "source": "Fuente: {src}.",
    "decision": "Recomendación de decisión: {note}",
    "level_same": "nivel de evidencia {o} sin cambios",
    "level_change": "nivel de evidencia {o} → {n}",
    "table_updated": (" Los valores de {labels} de esta página se actualizaron según el resultado de la nueva revisión; los valores "
                      "originales figuran en el Registro de revisión más abajo."),
    "rereviewed": "Marcado para nueva revisión → revisado de nuevo (ver el resultado de la nueva revisión)",
    "hdr": "Nivel de evidencia del encabezado recalculado a partir del Resumen rápido ({o} → {n})",
    "hdr_withdraw": "La predicción principal se retiró en la nueva revisión; nivel de evidencia del encabezado recalculado ({o} → {n})",
    "listed_under": ", ahora en \"{t}\"",
    "rr": "Nueva revisión: {v}, {c}",
    "tu": "; {l}: \"{a}\" → \"{b}\"",
    "desc": ("Descripción de la página: \"nivel de evidencia {o}\" cambiado a \"{n}\" (sigue el nivel del encabezado; el resto del "
             "texto no cambia y el original se guarda en el registro)"),
    "revised": " (revisado el {d}; la versión anterior se guarda en el registro)",
    "superseded": "Reemplazado por la tabla de registros generada por programa (antes: {a})",
    "regen": "Ya no aparece tras regenerar el informe ({d}: {n}; antes: {a})",
    "prog": "Ya no aparece tras una corrección del programa ({d}: {n}; antes: {a})",
    "wd": "Revisión retirada ({d}: {n}; antes: {a})",
    "intro": ("A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que "
              "usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; "
              "las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron."),
    "intro_levels": ("A continuación figura el registro de revisión de esta página; el nivel de evidencia del encabezado sigue el "
                     "Resumen rápido. Las predicciones del modelo, la tabla de resumen y las conclusiones no se reescribieron."),
    "intro_rr": ("A continuación figura el registro de revisión de esta página. Las correcciones se limitan a afirmaciones factuales "
                 "básicas y el texto de las predicciones del modelo no se reescribió; los niveles de evidencia y las decisiones solo "
                 "cambiaron por un resultado de nueva revisión (rebaja, elevación o retiro), con los valores originales más abajo."),
}

# ---------- 許可證（licenses、build_license_snapshot） ----------
MARKET_SEC = re.compile(r"^## Informaci[oó]n de Mercado en Colombia\s*$")
ID_RE = re.compile(r"\b\d{4,8}\b")  # INVIMA CUM expediente（2026-11-12 依證據包實測：4–8 碼數字；只驗市場段落表格第一欄）


def own_ids(tf):
    return sorted({str(r.get("license_id") or "").strip() for r in tf.get("records") or [] if r.get("license_id")})


PROGRAM_SCRIPT = "sync_license_tables.py"  # scripts/ 下產生程式許可證表的程式（build_license_snapshot 讀它的 rows_of／snap_extra）


def _slt():
    p = Path(__file__).resolve().parents[3] / "scripts" / PROGRAM_SCRIPT
    s = importlib.util.spec_from_file_location("co_sync_license_tables", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def program_block_problems(sec_lines, entry):
    """程式區塊（licenses:begin／end）＝依快照重算的結果（scripts/sync_license_tables.py 的 expected_block；列數依頁面上的列數，
    在 1～20 之間，快照存前 20 列）。段落裡有表卻沒有程式區塊＝AI 自由格式表沒換掉，也擋。"""
    S = _slt()
    has_b, has_e = S.BEGIN in sec_lines, S.END in sec_lines
    if has_b != has_e:
        return ["程式區塊標記不成對"]
    if not has_b:
        if any(l.startswith("|") for l in sec_lines) or any(l.strip() == S.NONE_LINE for l in sec_lines):
            return ["市場段落的許可證表不是程式區塊（跑 python3 scripts/sync_license_tables.py）"]
        return ["市場段落沒有程式許可證區塊（跑 python3 scripts/sync_license_tables.py）"]
    i, j = sec_lines.index(S.BEGIN), sec_lines.index(S.END)
    got = [x for x in sec_lines[i + 1:j] if x.strip()]
    errs = []
    if any(l.startswith("|") for k, l in enumerate(sec_lines) if k < i or k > j):
        errs.append("市場段落在程式區塊外另有表格")
    n = sum(1 for x in got[2:] if x.startswith("| ")) if got and got[0] == S.HEAD[0] else 0
    want = S.expected_block(entry, n)
    if got != want:
        k = next((k for k, (x, y) in enumerate(zip(got, want)) if x != y), min(len(got), len(want)))
        errs.append(f"程式區塊第 {k + 1} 行跟快照重算的結果不同（程式表被手改或資料已更新：跑 scripts/sync_license_tables.py）")
    return errs


# ---------- 刪改轉紀錄（reviews_from_edits） ----------
# 2026-10-31～11-06 的許可證刪改（git log docs/_drugs；排程狀態格 698d9250、欄位名統一、排除表、AI 重產、description、表格空行不算）
COMMITS = ["5fda915f", "d355c924", "e46b1db3"]
# 期間內以 AI 整份重產報告或套排除表重寫段落的提交
REGEN_COMMITS = ["a0de58db", "0832fc39", "7821f117", "79c1d685", "9bfc813e", "5e323b6e", "6897e7dd", "0c2d953a"]
SOURCES = [{"title": "INVIMA: Código Único de Medicamentos (datos.gov.co)", "url": "https://www.datos.gov.co/resource/i7cb-raxc.json"}]
SENT = re.compile(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ¿¡0-9(*"\[])|\n')
# 程式寫的句子（scripts/sync_license_tables.py 的 SHOW／NONE_LINE、known_use_pages 的部分紀錄提示）：轉紀錄與驗證時不當成正文
PROGRAM_LINES = [re.compile(r"^Se muestra(n)? (el único|los \d+|\d+ de (al menos )?\d+) registros? sanitarios? de este principio activo en los datos del INVIMA"),
                 re.compile(r"^No se encontraron registros sanitarios de este principio activo en los datos del INVIMA"),
                 re.compile(r"^Los datos solo contienen parte de los registros; la lista puede estar incompleta\.$")]
CLASSIFY = [
    ("tw", re.compile(r"Taiwan|Taiwán|TFDA", re.I)),
    ("cancel", re.compile(r"cancelad|vencid|no (está |esta )?(registrad|comercializad|autorizad|disponible)|sin registro|"
                          r"ning[uú]n registro|no (hay|tiene|cuenta con) registros?|no se (encontr|identific)\w* registro|"
                          r"no (hay|existe|tiene)[^.]{0,50}vigente|sin (productos?|registros?) vigentes?", re.I)),
    ("count", re.compile(r"\d+\s*registros?|todos? [^.]{0,40}vigente|\bvigente", re.I)),
    ("combo", re.compile(r"monocomponente|un solo componente|combinaci[oó]n|combinad", re.I)),
]
SUMMARY = "Eliminado: \"{text}\""
REGEN_NOTE = "el informe se regeneró en noviembre de 2026 y ya no contiene esta afirmación"


def reason_kind(reason):
    """人工清單（scripts/license_sentence_fixes.json）的中文理由 → 類別；判斷不了回 None（改用被刪文字分類）"""
    if re.search(r"台灣|TFDA|模板殘留", reason):
        return "tw"
    if re.search(r"誤判成 cancelled|cancelado|註銷|查無|未上市", reason):
        return "cancel"
    if re.search(r"單方|複方", reason):
        return "combo"
    return "count" if re.search(r"張|有效|總數|Vigente|矛盾", reason) else None


def _fig(fc):
    if not fc or fc.get("total") is None:
        return ""
    return (f" El medicamento tiene {fc['total']} registro{'s' if fc['total'] != 1 else ''} sanitario"
            f"{'s' if fc['total'] != 1 else ''} (vigentes: {fc.get('valid') or 0}); las cifras actuales están en el Resumen rápido "
            "y en la tabla de Información de Mercado en Colombia.")


def note_for(kind, date, fc):
    d = f"los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el {date}"
    if kind == "tw":
        return "Eliminado: texto residual de plantilla sobre la TFDA de Taiwán, que no corresponde a esta página de Colombia."
    if kind == "cancel":
        return (f"Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, "
                f"lo que no coincide con {d}." + _fig(fc))
    if kind == "count":
        return f"Eliminado: el número o el estado de los registros sanitarios no coincidía con {d}." + _fig(fc)
    if kind == "combo":
        return f"Eliminado: la descripción de productos monocomponente o en combinación no coincidía con {d}." + _fig(fc)
    return f"Eliminado: contradecía {d}." + _fig(fc)


# ---------- 原適應症交叉驗證（check_original_indications） ----------
ORIG_LABELS = ["Indicación Original", "Indicacion Original"]
ORIG_NONE_RE = re.compile(r"^\s*(no (registrad|disponible|consta)|sin (datos|registro)|ninguna|—|-|N/A)", re.I)
ORIG_SPLIT_RE = re.compile(r"[;,/()]+|\by\b|\bo\b", re.I)
