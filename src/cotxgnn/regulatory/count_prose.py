"""正文許可證張數的程式改寫（2026-11-24 建，用戶決定把 KrTxGNN／MyTxGNN 的做法移植到本站；結構照 MyTxGNN 的同名檔，規則是本站西班牙文句型）。

正文裡「N registros sanitarios (vigentes)」這類 INVIMA CUM 許可證張數敘述，由程式依許可證快照（snapshots/co_licenses.json.gz 的 facts）
改寫，每週資料更新後跟著改，不逐筆寫查核紀錄（同 Tw／Kr／My：程式改寫的張數敘述是程式產生的正文）。

只改「句型明確、數字確定是本藥許可證張數」的地方，其餘一律不動：
  - 句子要有許可證名詞（registro(s) sanitario(s)、licencia(s)、autorización(es)；在市場段落「Información de Mercado en Colombia」
    裡「N registros」也算），而且數字右邊緊接許可證名詞或狀態字（vigente、vencido…）；沒有交互作用、試驗、文獻等字樣。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、引言框、front matter；
    查核紀錄 replacement／anchor 所在的句子（改了紀錄會對不上）。
  - 整句不動（列在 skipped）：有保留（al menos、parcial、incomplet、puede haber más）、講證据包或查詢結果（datos compilados、consulta、
    devolvió、se encontraron、Evidence Pack）、相對數（otros、más、además de、restantes、adicionales）、劑型或廠商子集
    （tableta、cápsula、inyectable、crema、oftálmic…、laboratorio、S.A.S、pertenecen、fabricante、titular）；事實層 partial 的頁整頁不動。
  - 數字不動：顯示筆數（se muestran／se listan／la tabla／listados、「N de M」的 N）、劑量與年份。
角色看數字右側：cancelad／vencid／revocad／pérdida de fuerza→註銷；vigente(s)→有效；temporalmente no comercializad→暫時未上市；
de un solo principio activo／monocomponente／monofármaco／ingrediente único→單方（句中有 vigente 用有效單方）；en combinación／combinad→複方；
其餘→總數。
本站「vigente」的讀法（CLAUDE.md 2026-11-12 正文張數掃描的慣例）：INVIMA 的 Temp. no comerc - Vigente 法律上仍有效，所以原數字＝有效數或
有效＋暫時未上市數都算對、不改；要改時改成有效數（＝概覽表狀態列「registros vigentes」的數字）。
同一行只要有一句含許可證數字而被略過，整行都不動（免得前後句數字對不上）。
同一句另有明確的有效／註銷數字時，沒有限定詞的數字確定是總數。
數字已等於該角色的任一合理讀法（沒有限定詞的總數＝總數、有效數或有效＋暫時未上市數）就不動；不等於時各讀法相同才改，不同就列為 ambiguous。
原數字是 0 的句子（建立在 0 張前提上）不改、列為 zero-premise；跨過 1 張（1↔N，單複數與「único」要跟著改）不改、列為 plural（2026-11-25）；要改請寫查核紀錄。
前提檢查：句子說「todos (están) vigentes／ninguno cancelado」而事實有註銷、說全部是單方或全部是複方而事實不符時整句不動、列出（premise）。
"""
from __future__ import annotations

import re

from . import site as C

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ¿¡*\[(>-])")
NUM = re.compile(r"(?<![\w.,/-])(\d{1,3}(?:\.\d{3})+|\d+)(?![\w.,/%-]|[.,]\d)")
NOUN = r"(?:registros?(?:\s+sanitarios?)?|licencias?|autorizaci(?:ón|ones|on)|productos?|presentaciones?)"
LICENSE = re.compile(r"\bregistros?\s+sanitarios?\b|\blicencias?\b|\bautorizaci(ón|ones|on)\b|\bINVIMA\b|"
                     r"\d+\s+registros?\b(?!\s+de\s+(ensayos?|estudios?|pacientes?|casos?))", re.I)
MKT_NOUN = re.compile(r"\d+\s+(registros?|productos?)\b", re.I)
NOT_LICENSE = re.compile(r"interacci|ensayo|estudio|art[ií]culo|PMID|NCT|pacientes?|casos?\b|efectos? adversos?|\bmg\b|\bml\b|%|"
                         r"\baños?\b|\bmeses\b|semanas?|d[ií]as?\b|candidat|predicci|predich|puntuaci|score|rank|farmacolog|blancos?\b|"
                         r"receptor|DrugBank|ChEMBL|PubMed|ClinicalTrials|publicaci", re.I)
HEDGED = re.compile(r"al menos|parcial|incomplet|puede haber m[aá]s|pueden existir|podr[ií]a|posiblemente|datos compilados|compilad|"
                    r"Evidence Pack|paquete de evidencia|consulta|devolvi|se (encontraron|identificaron|registraron)|identificad|"
                    r"\botr[oa]s\b|\bm[aá]s\b|adem[aá]s de|restantes?|adicional|resto|incluid|entre ellos|"
                    r"veterinari|exportaci|laboratori|\bS\.?A\.?S?\b|Ltda|pertenec|fabricant|titular|"
                    r"tableta|c[aá]psula|inyectable|soluci[oó]n|crema|jarabe|suspensi[oó]n|oft[aá]lmic|t[oó]pic|oral\b|gel\b|"
                    r"ung[uü]ento|polvo|ampolla|vial|parche|aerosol|inhalad|gotas|forma farmac", re.I)
DISPLAY = re.compile(r"(se muestran?|se listan?|la tabla|listad[oa]s|anteriores|siguientes|arriba|abajo|mostrad[oa]s|principales)", re.I)
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)
VIG = r"(?:vigentes?|en vigor|activ[oa]s?|v[aá]lid[oa]s?)"
CANC = r"(?:cancelad[oa]s?|vencid[oa]s?|revocad[oa]s?|anulad[oa]s?|con p[eé]rdida de fuerza)"


def _role(s, a, b):
    left, right = s[max(0, a - 30):a].lower(), s[b:b + 60].lower()
    if re.match(r"\s*de\s+(los\s+|las\s+)?\d", right):
        return "display"
    # 2026-11-25：「N licencias válidas de M」「N registros vigentes de M」的 M 是總數（之前沒有角色，只改了 N：iohexol「2 licencia válida de 1」）
    if re.search(rf"{VIG}\s+de\s+(los\s+|las\s+)?$", left):
        return "total"
    # 「N de M」「los N principales de M」的 M 是總數（或有效數），不是顯示筆數：照右側判斷
    if DISPLAY.search(left) and not re.search(r"\bde\s+(los\s+|las\s+)?$", left):
        return "display"
    if DISPLAY.search(right[:30]) and not re.match(rf"\s*{NOUN}", right):
        return "display"
    near = right[:55]
    if re.match(rf"\s*(?:{NOUN}\s+)?(?:\w+\s+){{0,2}}(?:est[aá]n\s+|figuran\s+(?:como\s+)?|son\s+)?{CANC}", near):
        return "cancelled"
    if re.match(rf"\s*(?:{NOUN}\s+)?(?:\w+\s+){{0,2}}(?:est[aá]n\s+)?temporalmente no comercializad", near):
        return "nm"
    if re.match(rf"\s*(?:{NOUN}\s+)?(?:\w+\s+){{0,3}}(?:de\s+)?(?:un solo principio activo|un solo componente|monocomponentes?|monof[aá]rmacos?|"
                r"ingrediente [uú]nico|principio activo [uú]nico|[uú]nico principio activo)", near):
        return "single"
    if re.match(rf"\s*(?:{NOUN}\s+)?(?:\w+\s+){{0,2}}(?:son\s+|en\s+|de\s+)?(?:combinaci[oó]n|combinad[oa]s|asociaci[oó]n)", near):
        return "combo"
    if re.match(rf"\s*(?:{NOUN}\s+)?(?:colombianos?\s+|locales\s+|del INVIMA\s+)?(?:est[aá]n\s+|figuran\s+como\s+|siguen\s+)?(?:actualmente\s+)?{VIG}\b", near):
        return "valid"
    if re.match(rf"\s*{NOUN}\b", right) or re.search(r"(total de|en total|un total de|cuenta con|tiene|existen|hay|con|suma)\s+$", left):
        if re.match(rf"\s*{NOUN}\b", right):
            return "total"
    return None


def _readings(role, f, sent, explicit=False):
    t, v, c, nm = f.get("total"), f.get("valid"), f.get("cancelled"), f.get("not_marketed") or 0
    st, vs = f.get("single_total"), f.get("valid_single")
    vlegal = None if v is None else v + nm
    validctx = bool(re.search(r"\bvigentes?\b|\bv[aá]lid[oa]s?\b", sent, re.I))
    if role == "cancelled":
        return {c}, c
    if role == "nm":
        return {nm}, nm
    if role == "valid":
        return {v, vlegal}, v
    if role == "single":
        if validctx:
            return {vs}, vs
        return {st, vs}, st if st == vs else None
    if role == "combo":
        ct = None if t is None or st is None else t - st
        cv = None if v is None or vs is None else v - vs
        if validctx:
            return {cv}, cv
        return {ct, cv}, ct if ct == cv else None
    if explicit:  # 同一句另有明確的有效／註銷數字：沒有限定詞的那個就是總數
        return {t}, t
    return {t, v, vlegal}, t if t == v else None


def _premise_ok(sent, f):
    lo = sent.lower()
    if re.search(r"\b(tod[oa]s|ambos|ambas)\b[^.;]{0,60}\bvigentes?\b|ning[uú]n[oa]? (\w+ ){0,3}(est[aá] )?(cancelad|vencid|revocad)|"
                 r"sin (\w+ ){0,2}(cancelad|vencid|cancelaciones)", lo) \
            and ((f.get("valid") or 0) + (f.get("not_marketed") or 0) != f.get("total") or f.get("cancelled")):
        return False
    if re.search(r"\b(tod[oa]s|ambos|ambas)\b[^.;]{0,60}(un solo principio activo|monocomponente|monof[aá]rmaco|ingrediente [uú]nico)", lo):
        if f.get("single_total") != f.get("total"):
            return False
    if re.search(r"\b(tod[oa]s|ambos|ambas)\b[^.;]{0,60}(combinaci[oó]n|combinad)", lo):
        if f.get("single_total"):
            return False
    return True


def rewrite_sentence(sent, f, market=False):
    """回傳 (新句子, 跳過理由或 None)。"""
    if not NUM.search(sent) or not (LICENSE.search(sent) or (market and MKT_NOUN.search(sent))):
        return sent, None
    if NOT_LICENSE.search(sent):
        return sent, None
    found = [(m, _role(sent, m.start(), m.end())) for m in NUM.finditer(sent)]
    if not any(r not in (None, "display") for _, r in found):
        return sent, None
    if HEDGED.search(sent):
        return sent, "hedged/subset"
    explicit = any(r in ("valid", "cancelled", "nm") for _, r in found)
    subs = []
    for m, role in found:
        if role in (None, "display"):
            continue
        old = int(m.group(1).replace(".", ""))
        ok, v = _readings(role, f, sent, explicit)
        if old in ok:
            continue
        if v is None:
            return sent, "ambiguous"
        if old == 0:
            return sent, "zero-premise"
        if (old == 1) != (v == 1):  # 2026-11-25：跨過 1 張（名詞、動詞、「único」的單複數要跟著改）不改，列 plural
            return sent, "plural"
        subs.append((m, v))
    if not subs:
        return sent, None
    if not _premise_ok(sent, f):
        return sent, "premise"
    out, pos = [], 0
    for m, v in subs:
        out.append(sent[pos:m.start(1)])
        out.append(f"{v:,}".replace(",", ".") if v >= 1000 else str(v))
        pos = m.end(1)
    out.append(sent[pos:])
    new = "".join(out)
    # 單複數：1 registro／N registros（只改數字緊接的名詞與 vigente，其餘不動）
    new = re.sub(r"\b1 (registro)s( sanitario)s\b", r"1 \1\2", new)
    new = re.sub(r"\b1 (registro)s\b", r"1 \1", new)
    new = re.sub(r"\b1 (registros? sanitarios?|registro) vigentes\b", r"1 \1 vigente", new)
    new = re.sub(r"\b([2-9]|\d{2,}) (registro)( sanitario)?( vigente)?\b(?!s)",
                 lambda m: f"{m.group(1)} {m.group(2)}s{(m.group(3) or '') and m.group(3) + 's'}{(m.group(4) or '') and m.group(4) + 's'}", new)
    return new, None


def _line(ln, f, protect, skipped, market=False):
    if ln.startswith(("|", "#", ">")) or not ln.strip():
        return ln
    parts = SENT_SPLIT.split(ln)
    seps = SENT_SPLIT.findall(ln)
    new, held = [], False
    for s in parts:
        if any(p and (p in s or s in p) for p in protect):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f, market)
        if why:
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if held:  # 同一行有句子判斷不了：整行不動，免得改了一句、旁邊的句子對不上
        return ln
    out = new[0]
    for sep, s in zip(seps, new[1:]):
        out += sep + s
    return out


def rewrite(text, facts, protect=()):
    """text：整頁 markdown。facts：快照的 facts。回傳 (新內容, skipped)。front matter、查核框、程式區塊、表格不動。"""
    skipped = []
    if not facts or facts.get("partial") or facts.get("total") is None:
        return text, skipped
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines, market = [], False
    for ln in body.split("\n"):
        if ln.startswith("## "):
            market = bool(C.MARKET_SEC.match(ln))
        lines.append(ln if "\x00" in ln else _line(ln, facts, protect, skipped, market))
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
