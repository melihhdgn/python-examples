import pandas as pd
import numpy as np
import json
import re
from pandas import json_normalize
from sklearn.preprocessing import MinMaxScaler

#burda manuel doldurma yok outlier_detection kısmında all_outlier.json kısmına ekledik ordan çekiyoruz hataları.uyumsuzluk harici

def fix_numeric_type_mismatches(json_path="veri_temiz.json", outliers_path="all_outliers.json"):
    """
    Sayısal olması gereken sütunlarda metin varsa,
    o hücreleri önceki veya sonraki geçerli sayısal değerle doldurur.
    """
    manuel_duzeltilecek_sutunlar = []  

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    df = json_normalize(data)

    with open(outliers_path, encoding="utf-8") as f:
        issues = json.load(f).get("type_mismatches", {}).get("text_in_numeric", {})

    changes = 0

    for col, idxs in issues.items():
        if col not in manuel_duzeltilecek_sutunlar:
            continue
        for idx in idxs:
            val = df.at[idx, col]
            try:
                float(val)  # Eğer sayıya dönüşebiliyorsa sorun yok, atla
                continue
            except:
                pass

            replacement_value = None
            # Önceki geçerli sayısal değeri ara
            for prev_idx in range(idx - 1, -1, -1):
                try:
                    candidate = df.at[prev_idx, col]
                    if pd.notna(candidate):
                        replacement_value = float(candidate)
                        break
                except:
                    continue

            # Yoksa sonraki geçerli sayısal değeri ara
            if replacement_value is None:
                for next_idx in range(idx + 1, len(df)):
                    try:
                        candidate = df.at[next_idx, col]
                        if pd.notna(candidate):
                            replacement_value = float(candidate)
                            break
                    except:
                        continue

            if replacement_value is not None:
                df.at[idx, col] = replacement_value
                changes += 1

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=4)

    print(f"✅ {changes} adet sayısal tip uyumsuzluğu düzeltildi.")


def fix_text_type_mismatches(json_path="veri_temiz.json", outliers_path="all_outliers.json"):
    """
    Metin olması gereken sütunlarda sayısal değer varsa,
    o hücreleri önceki veya sonraki geçerli metin değeriyle doldurur.
    """
    manuel_duzeltilecek_sutunlar = []  # Örnek: ["kategori", "renk"]

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    df = json_normalize(data)

    with open(outliers_path, encoding="utf-8") as f:
        issues = json.load(f).get("type_mismatches", {}).get("numeric_as_text", {})

    changes = 0

    for col, idxs in issues.items():
        if col not in manuel_duzeltilecek_sutunlar:
            continue
        for idx in idxs:
            val = df.at[idx, col]
            # Metin sütunu olması gereken yerde sayısal ise düzelt
            try:
                float(val)
                # Sayı ise düzeltme yapacak, devam
            except:
                continue  # Sayı değilse sorun yok, atla

            replacement_value = None
            # Önceki geçerli metin değeri ara
            for prev_idx in range(idx - 1, -1, -1):
                candidate = df.at[prev_idx, col]
                if pd.notna(candidate) and isinstance(candidate, str) and candidate.strip() != "":
                    replacement_value = candidate
                    break

            # Yoksa sonraki geçerli metin değeri ara
            if replacement_value is None:
                for next_idx in range(idx + 1, len(df)):
                    candidate = df.at[next_idx, col]
                    if pd.notna(candidate) and isinstance(candidate, str) and candidate.strip() != "":
                        replacement_value = candidate
                        break

            if replacement_value is not None:
                df.at[idx, col] = replacement_value
                changes += 1

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=4)

    print(f"✅ {changes} adet metin tip uyumsuzluğu düzeltildi.")

def fill_numeric_nulls_and_outliers(json_path="veri_temiz.json", outliers_path="all_outliers.json"):
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    df = json_normalize(data)

    with open(outliers_path, encoding="utf-8") as f:
        out = json.load(f)                    #-----> aykırı ve boş değerler bir önceki ve sonrakinden alınarak doldurulur
    num_issues = out.get("numeric_outliers", {})

    for col, idxs in num_issues.items():
        for idx in idxs:
            if col in df.columns and idx < len(df):
                df.at[idx, col] = np.nan

    
    df = df.ffill().bfill()

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=4)

    print(f"✅ Sayısal boş/aykırı değer dolduruldu: '{json_path}' güncellendi.")


def fill_categorical_outliers_with_mode(json_path="veri_temiz.json", outliers_path="all_outliers.json"):

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    df = json_normalize(data)

    with open(outliers_path, encoding="utf-8") as f:
        outliers = json.load(f)
    cat_outliers = outliers.get("categorical_outliers", {})

    for col, idxs in cat_outliers.items():
        if col in df.columns:
            mode_val_series = df[col].mode(dropna=True)
            if not mode_val_series.empty:
                mode_val = mode_val_series[0]

                for idx in idxs:
                    if 0 <= idx < len(df):
                        df.at[idx, col] = mode_val

                df[col].fillna(mode_val, inplace=True)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=4)

    print(f"✅ Kategorik aykırı ve boş değerler mod ile dolduruldu, '{json_path}' güncellendi.")


def fill_bool_nulls_and_outliers(json_path="veri_temiz.json", outliers_path="all_outliers.json"):

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    df = json_normalize(data)

    with open(outliers_path, encoding="utf-8") as f:
        outliers = json.load(f)
    bol_outlier = outliers.get("bool_outliers", {})

    for col, idxs in bol_outlier.items():
        if col in df.columns:
            mode_val = df[col].mode(dropna=True)        #---------> boolean aykırı ve boş değerleri mod ile doldurur günceller
            if not mode_val.empty:
                mode_val = mode_val[0]

                # Aykırı indekslerde mod ile değiştir
                for idx in idxs:
                    if 0 <= idx < len(df):
                        df.at[idx, col] = mode_val

                # Boş değerleri mod ile doldur
                df[col].fillna(mode_val, inplace=True)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=4)

    print(f"✅ Bool tipi aykırı + boş değerler mod ile dolduruldu ve '{json_path}' güncellendi.")

def fill_date_nulls_and_outliers(json_path="veri_temiz.json", outliers_path="all_outliers.json"):

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    df = json_normalize(data)

    with open(outliers_path, encoding="utf-8") as f:
        outliers = json.load(f)
    date_outliers = outliers.get("date_outliers", {})

    # Aykırı indekslerde NaT yap ve sütunu datetime yap
    for col, idxs in date_outliers.items():
        if col in df.columns:
            # Tarih sütununu datetime formatına çevir, aykırı değerler NaT olacak
            df[col] = pd.to_datetime(df[col], errors="coerce")
            for idx in idxs:
                if 0 <= idx < len(df):
                    df.at[idx, col] = pd.NaT

    # Tarih sütunlarını öndolgu ve sondolgu ile tamamla
    for col in date_outliers.keys():
        if col in df.columns:
            # Eğer daha önce datetime'a çevrilmediyse çevir
            if not pd.api.types.is_datetime64_any_dtype(df[col]):
                df[col] = pd.to_datetime(df[col], errors="coerce")
            df[col] = df[col].ffill().bfill()

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=4)

    print(f"✅ Tarihi boş/aykırı değerler dolduruldu ve '{json_path}' güncellendi.")