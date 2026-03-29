#!/usr/bin/env python3
"""處理哥倫比亞 INVIMA 藥品資料

從 Socrata SODA API (datos.gov.co) 下載藥品註冊資料並轉換為 JSON。

使用方法:
    uv run python scripts/process_fda_data.py

資料來源:
    https://datos.gov.co/resource/i7cb-raxc.json

產生檔案:
    data/raw/co_fda_drugs.json
"""

import json
from pathlib import Path

import pandas as pd
import requests
import yaml


def load_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def download_invima_data(output_path: Path) -> Path:
    """從 Socrata SODA API 下載 INVIMA 藥品資料

    Socrata API 預設每次回傳 1000 筆，使用 $offset 和 $limit 分頁。

    Args:
        output_path: JSON 輸出路徑

    Returns:
        下載的檔案路徑
    """
    config = load_config()
    base_url = config["data_source"]["url"]

    print("正在從 Socrata SODA API 下載 INVIMA 資料...")
    print(f"API URL: {base_url}")

    all_records = []
    offset = 0
    limit = 1000  # Socrata default max per request

    while True:
        params = {
            "$limit": limit,
            "$offset": offset,
            "$order": "expediente",
        }
        print(f"  下載 offset={offset}...", end=" ", flush=True)

        try:
            response = requests.get(base_url, params=params, timeout=60)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"\n下載失敗 (offset={offset}): {e}")
            if all_records:
                print(f"已收集 {len(all_records)} 筆資料，繼續處理...")
                break
            raise

        batch = response.json()

        if not batch:
            print("無更多資料")
            break

        all_records.extend(batch)
        print(f"取得 {len(batch)} 筆 (累計: {len(all_records)})")

        if len(batch) < limit:
            break

        offset += limit

    print(f"\n下載完成，共 {len(all_records)} 筆資料")

    # 確保輸出目錄存在
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_records, f, ensure_ascii=False, indent=2)

    print(f"已儲存至: {output_path}")
    return output_path


def process_invima_data(input_path: Path, output_path: Path) -> Path:
    """處理 INVIMA JSON 資料

    Socrata API 已回傳扁平 JSON，只需清理和正規化。

    Args:
        input_path: 原始 JSON 檔案路徑
        output_path: 處理後 JSON 輸出路徑

    Returns:
        輸出檔案路徑
    """
    config = load_config()

    print(f"讀取資料檔案: {input_path}")

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"原始資料筆數: {len(data)}")

    df = pd.DataFrame(data)

    # 清理資料
    df = df.fillna("")

    # 正規化欄位名稱（Socrata 回傳小寫欄位名）
    # fields.yaml 已使用小寫，所以不需要額外轉換

    data = df.to_dict(orient="records")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"儲存至: {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"完成！共 {len(data)} 筆藥品資料")

    # 顯示統計
    print_statistics(df, config)

    return output_path


def print_statistics(df: pd.DataFrame, config: dict):
    """印出資料統計"""
    fm = config["field_mapping"]
    status_field = fm["status"]
    ingredients_field = fm["ingredients"]

    print("\n" + "=" * 50)
    print("資料統計")
    print("=" * 50)

    if status_field in df.columns:
        print(f"\n註冊狀態分布:")
        status_counts = df[status_field].value_counts()
        for status, count in status_counts.items():
            print(f"  {status}: {count:,}")

    if ingredients_field in df.columns:
        with_ingredients = (df[ingredients_field] != "").sum()
        print(f"\n有活性成分: {with_ingredients:,} ({with_ingredients/len(df)*100:.1f}%)")


def main():
    print("=" * 60)
    print("處理哥倫比亞 INVIMA 藥品資料")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    raw_json = raw_dir / "invima_medicamentos_raw.json"
    output_path = raw_dir / "co_fda_drugs.json"

    # 確保 raw 目錄存在
    raw_dir.mkdir(parents=True, exist_ok=True)

    # 下載資料（如果不存在）
    if not raw_json.exists():
        download_invima_data(raw_json)
    else:
        print(f"使用已存在的原始資料: {raw_json}")

    # 處理資料
    process_invima_data(raw_json, output_path)

    print()
    print("下一步: 準備詞彙表資料")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
