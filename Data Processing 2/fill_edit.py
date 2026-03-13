import pandas as pd
import numpy as np
import json
import re
from pandas import json_normalize
from sklearn.preprocessing import MinMaxScaler


def normalize(df, outpath):
    scale_columns = ["fiyat.24", "fiyat.25", "fiyat.26"]
    scaler = MinMaxScaler()  
    for col in scale_columns:
        df[[col]] = scaler.fit_transform(df[[col]])
    df.to_json(outpath, orient="records", force_ascii=False)


def save_all_outliers(df, out_json_path="all_outliers.json", min_freq_ratio=0.01):
    out = {
        "numeric_outliers": {},
        "categorical_outliers": {},
        "type_mismatches": {
            "text_in_numeric": {},
            "numeric_as_text": {}
        }
    }

    # sayısal aykırılar
    num_cols = df.select_dtypes(include=np.number).columns
    for col in num_cols:
        Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
        IQR = Q3 - Q1
        mask = (df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))
        if mask.any():
            out["numeric_outliers"][col] = df.index[mask].tolist()

        # sayısal olması gereken yerde string varsa
        textmask = df[col].apply(lambda x: isinstance(x, str) and not re.match(r"^-?\d+(\.\d+)?$", x))
        if textmask.any():
            out["type_mismatches"]["text_in_numeric"][col] = df[textmask].index.tolist()

    # kategorik aykırılar + tip hataları
    cat_cols = [
        col for col in df.columns
        if df[col].dtype == 'object' and df[col].dropna().apply(lambda x: isinstance(x, str)).all()
    ]
    for col in cat_cols:
        freqs = df[col].value_counts(normalize=True)
        rare = freqs[freqs < min_freq_ratio].index.tolist()
        if rare:
            out["categorical_outliers"][col] = df[df[col].isin(rare)].index.tolist()

        # kategorik içinde sayı var mı?
        masknum = df[col].astype(str).apply(lambda x: bool(re.fullmatch(r"^-?\d+(\.\d+)?$", x)))
        if masknum.any():
            out["type_mismatches"]["numeric_as_text"][col] = df[masknum].index.tolist()

    with open(out_json_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=4)

    print(f"✅ 'all_outliers.json' oluşturuldu ve tip hataları eklendi.")

def fix_type_mismatches(json_path="veri_temiz.json", outliers_path="all_outliers.json"):
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    df = json_normalize(data)

    with open(outliers_path, encoding="utf-8") as f:
        issues = json.load(f).get("type_mismatches", {})

    changes = 0

    for col, idxs in issues.get("text_in_numeric", {}).items():
        for idx in idxs:
            try:
                clean = re.sub(r"[^\d\.\-]", "", str(df.at[idx, col]))
                df.at[idx, col] = float(clean)
                changes += 1
            except Exception:
                pass

    for col, idxs in issues.get("numeric_as_text", {}).items():
        for idx in idxs:
            try:
                df.at[idx, col] = str(df.at[idx, col])
                changes += 1
            except Exception:
                pass

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=4)

    print(f"✅ {changes} tip uyumsuzluk düzeltildi, '{json_path}' güncellendi.")

def fill_numeric_nulls_and_outliers(json_path="veri_temiz.json", outliers_path="all_outliers.json"):
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    df = json_normalize(data)

    with open(outliers_path, encoding="utf-8") as f:
        out = json.load(f)
    num_issues = out.get("numeric_outliers", {})

    for col, idxs in num_issues.items():
        for idx in idxs:
            if col in df.columns and idx < len(df):
                df.at[idx, col] = np.nan

    num_cols = df.select_dtypes(include=np.number).columns
    df[num_cols] = df[num_cols].ffill().bfill()

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

    # Kategorik sütunları belirle
    categorical_cols = [
        col for col in df.columns
        if df[col].dtype == 'object' and df[col].dropna().apply(lambda x: isinstance(x, str)).all()
    ]

    for col in categorical_cols:
        if col in df.columns:
            mode_val = df[col].mode(dropna=True)
            if not mode_val.empty:
                mode_val = mode_val[0]

                # Aykırı değerleri ve NaN'leri mod ile değiştir
                outlier_indices = cat_outliers.get(col, [])
                for idx in outlier_indices:
                    if idx < len(df):
                        df.at[idx, col] = mode_val

                # NULL (NaN) değerleri de doldur
                df[col] = df[col].fillna(mode_val)

    # JSON'a geri yaz
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=4)

    print(f"✅ Kategorik aykırı + boş değerler mod ile dolduruldu ve '{json_path}' dosyası güncellendi.")


