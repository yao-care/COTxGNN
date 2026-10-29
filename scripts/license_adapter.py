"""CO（INVIMA CUM，datos.gov.co Socrata）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

INVIMA 把 CUM 依狀態拆成四個公開資料集（免金鑰）：
  i7cb-raxc 有效（Vigente）、vgr4-gemg 展延中（En tramite renov）、spzp-dfuc 其他狀態、vwwf-4ftk 過期（Vencido）。
以 expediente（＝證據包 license_id）彙總，對應到 reviewer 的狀態：
  valid：Vigente、En tramite renov
  not_marketed：Temp. no comerc - Vigente、Temp. no comercializado - En Trámite Renov、Comercializado solo por Exportacion
  cancelled：Vencido、Cancelado、Revocado、Suspendido、Abandono、Desistido、Negado、Perdida Fuerza Ejec
同一 expediente 出現在多個狀態時取 valid > not_marketed > cancelled。「No Aplica Registro」不採用。
寫回紀錄：status＝INVIMA 原文、license_status＝對應狀態（reviewer 優先讀 license_status，西語「Vencido」不在註銷字樣裡）。
"""
import time

import requests

RAW_FILE = "raw/invima_cum_estado.json"
SETS = {"i7cb-raxc": "vigentes", "vgr4-gemg": "renovacion", "spzp-dfuc": "otros", "vwwf-4ftk": "vencidos"}
CLASS = {
    "vigente": "valid", "en tramite renov": "valid",
    "temp. no comerc - vigente": "not_marketed", "temp. no comercializado - en trámite renov": "not_marketed",
    "comercializado solo por exportacion": "not_marketed",
    "vencido": "cancelled", "cancelado": "cancelled", "revocado": "cancelled", "suspendido": "cancelled",
    "abandono": "cancelled", "desistido": "cancelled", "negado": "cancelled", "perdida fuerza ejec": "cancelled",
}
RANK = {"valid": 3, "not_marketed": 2, "cancelled": 1}


def _get(url, params):
    for attempt in range(4):
        try:
            r = requests.get(url, params=params, timeout=120)
            r.raise_for_status()
            return r.json()
        except Exception:
            if attempt == 3:
                raise
            time.sleep(10 * (attempt + 1))


def fetch():
    out = []
    for ds, name in SETS.items():
        off, n = 0, 0
        while True:
            rows = _get(f"https://www.datos.gov.co/resource/{ds}.json",
                        {"$select": "expediente,estadoregistro", "$group": "expediente,estadoregistro",
                         "$order": "expediente", "$limit": 50000, "$offset": off})
            for x in rows:
                out.append({"expediente": str(x.get("expediente") or "").strip(), "estado": (x.get("estadoregistro") or "").strip(), "dataset": name})
            n += len(rows)
            if len(rows) < 50000:
                break
            off += 50000
        if n == 0:
            raise RuntimeError(f"資料集 {ds}（{name}）回傳 0 筆")
    return out


def validate(new, old):
    p = []
    unknown = sorted({r["estado"] for r in new if r["estado"].lower() not in CLASS and r["estado"] != "No Aplica Registro"})
    if unknown:
        p.append(f"出現沒對應過的狀態：{unknown[:5]}")
    if sum(1 for r in new if r["dataset"] == "vigentes") < 5000:
        p.append("有效資料集少於 5,000 個 expediente，疑似來源改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    idx = {}
    for r in new:
        c = CLASS.get(r["estado"].lower())
        if not c or not r["expediente"]:
            continue
        cur = idx.get(r["expediente"])
        if cur is None or RANK[c] > RANK[cur[1]]:
            idx[r["expediente"]] = (r["estado"], c)
    return idx


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    text, cls = new
    if rec.get("status") == text and rec.get("license_status", "valid" if text == "Vigente" else None) == cls:
        return False  # 舊紀錄沒有 license_status 但原文是 Vigente：意義相同，不算變動
    rec["status"], rec["license_status"] = text, cls
    return True
