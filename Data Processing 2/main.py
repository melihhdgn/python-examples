import pandas as pd
import numpy as np
import json
from pandas import json_normalize
from fill_edit import (
    save_all_outliers,
    fix_type_mismatches,
    fill_numeric_nulls_and_outliers,
    fill_categorical_outliers_with_mode
)
from grafik import goster_grafikler 
from fill_edit import normalize

def fill_missing_json(json_path, output_path="veri_temiz.json"):
    def get_nested(row, keys):
        ref = row
        for k in keys:
            if isinstance(ref, dict) and k in ref:
                ref = ref[k]
            else:
                return None
        return ref

    with open(json_path, "r", encoding="utf-8") as f:
        contents = json.load(f)

    def extract_all_keys(d, prefix=''):
        keys = []
        for k, v in d.items():
            full_key = f"{prefix}.{k}" if prefix else k
            keys.append(full_key)
            if isinstance(v, dict):
                keys.extend(extract_all_keys(v, full_key))
        return keys

    all_cols = set()
    for row in contents:
        all_cols.update(extract_all_keys(row))
    all_cols = list(all_cols)

    for i, row in enumerate(contents):
        for col in all_cols:
            keys = col.split('.')
            ref = row
            for k in keys[:-1]:
                if k not in ref or not isinstance(ref[k], dict):
                    ref[k] = {}
                ref = ref[k]
            last_key = keys[-1]
            if last_key not in ref:
                value = None
                if i > 0:
                    value = get_nested(contents[i - 1], keys)
                if value is None and i < len(contents) - 1:
                    value = get_nested(contents[i + 1], keys)
                ref[last_key] = value if value is not None else None

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(contents, f, ensure_ascii=False, indent=4)

    return output_path

def report_missing(json_path):
    df = json_normalize(json.load(open(json_path, encoding="utf-8")))
    missing_counts = df.isnull().sum()
    missing_counts = missing_counts[missing_counts > 0].sort_values(ascending=False)

    if missing_counts.empty:
        print("✅ Veride eksik alan bulunmamaktadır.")
    else:
        print(f"⚠️ Toplam {len(missing_counts)} sütunda eksik veri bulundu:")
        print(missing_counts)
        missing_percentage = (missing_counts / len(df)) * 100
        print("\n📊 Eksik veri yüzdeleri:")
        print(missing_percentage.round(2).astype(str) + "%")

def save_categorical_columns_to_txt(df, output_txt_path, output_txt_path2):
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    with open(output_txt_path, "w", encoding="utf-8") as f:
        for col in categorical_cols:
            f.write(col + "\n")
    numeric_cols = df.select_dtypes(include=np.number).columns
    with open(output_txt_path2, "w", encoding="utf-8") as f:
        for col in numeric_cols:
            f.write(col + "\n")
    print(f"📁 {len(categorical_cols)} tane kategorik sütun '{output_txt_path}' dosyasına kaydedildi.")
    print(f"📁 {len(numeric_cols)} tane numeric sütun '{output_txt_path2}' dosyasına kaydedildi.")

def detect_categorical_outliers(df, min_freq_ratio=0.01):
    aykiri_degerler = {}
    categor_cols = [
        col for col in df.columns
        if df[col].dtype == 'object' and df[col].dropna().apply(lambda x: isinstance(x, str)).all()
    ]
    for sutun in categor_cols:
        frekanslar = df[sutun].value_counts(normalize=True)
        nadir = frekanslar[frekanslar < min_freq_ratio].index.tolist()
        if nadir:
            aykiri_degerler[sutun] = nadir

    if aykiri_degerler:
        print("🚨 Aykırı (nadir) kategorik değerler:")
        for sutun, degerler in aykiri_degerler.items():
            print(f"→ {sutun}: {degerler}")
    else:
        print("✅ Aykırı kategorik değer bulunamadı.")

def detect_numeric_outliers(df):
    numeric_cols = df.select_dtypes(include=np.number).columns
    num_outliers = {}
    for col in numeric_cols:
        Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
        IQR = Q3 - Q1
        mask = (df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))
        if mask.any():
            num_outliers[col] = df.index[mask].tolist()
    return num_outliers

def normalize_and_cast(df):
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")
    return df

def main():
    temiz_json = fill_missing_json("örnek.json")
    print("✅ Eksik alanlar dolduruldu.")

    # JSON sonrası normalize & cast
    df = pd.json_normalize(json.load(open(temiz_json, encoding="utf-8")))
    df = normalize_and_cast(df)

    print("📊 Sütun tipleri:")
    print(df.dtypes)

    if input("➡️ Eksik veri raporunu görmek ister misiniz? (e/h): ").lower() == "e":
        report_missing(temiz_json)

    if input("➡️ Kategorik sütunları .txt'e kaydedelim mi? (e/h): ").lower() == "e":
        save_categorical_columns_to_txt(df, "kategorik_sutunlar.txt", "numeric_sutunlar.txt")

    if input("➡️ Kategorik aykırı değerleri tespit edelim mi? (e/h): ").lower() == "e":
        detect_categorical_outliers(df)

    if input("➡️ Sayısal aykırı değerleri tespit edelim mi? (e/h): ").lower() == "e":
        nums = detect_numeric_outliers(df)
        if nums:
            print("🚨 Sayısal sütunlarda aykırı değer indeksleri:")
            for col, idxs in nums.items():
                print(f"→ {col}: {idxs}")
        else:
            print("✅ Sayısal sütunlarda aykırı değer bulunmadı.")

    if input("➡️ Aykırı değerleri JSON'a kaydedelim mi? (e/h): ").lower() == "e":
        save_all_outliers(df)

    if input("➡️ Tip uyumsuzluklarını düzeltelim mi? (e/h): ").lower() == "e":
        fix_type_mismatches()

    if input("➡️ Sayısal boş/aykırı değerleri dolduralım mı? (e/h): ").lower() == "e":
        fill_numeric_nulls_and_outliers()

    if input("➡️ Kategorik aykırı değerleri mod ile dolduralım mı? (e/h): ").lower() == "e":
        fill_categorical_outliers_with_mode()
        
    if input("➡️ Veri analizi için grafik istermisin ?  (e/h): ").lower() == "e":
        goster_grafikler()
    
    if input ("➡️ Verileri ölçeklendirmek için normalize yapmak istermisiniz? (e/h)").lower() == "e":
        normalize(df, "veri_temiz.json")
        print("✅ Veriler normalize edildi ve 'veri_normalize.json' olarak kaydedildi.")

if __name__ == "__main__":
    main()
