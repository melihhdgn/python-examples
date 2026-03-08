import pandas as pd
import numpy as np
import json
import re
from datetime import datetime
from pandas import json_normalize
from sklearn.preprocessing import MinMaxScaler

def detect_categorical_outliers(df, min_freq_ratio=0.01):
                                                               #Nadir kategorik değerleri tespit eder. yöntemi çok olan toplluktan uzak olanlar nadirdir.
    categoric_cols = ["melih"] #manuel
    outliers = {}

    for col in categoric_cols:
        freqs = df[col].value_counts(normalize=True)
        rare = freqs[freqs < min_freq_ratio].index.tolist()
        if rare:
            outliers[col] = rare
    return outliers

def detect_numeric_outliers(df):
    #                      A                  IQR yöntemine göre sayısal aykırı değerleri tespit eder.
    outliers = {}
    numeric_cols = [] #manuel doldur
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        mask = (df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))
        if mask.any():
            outliers[col] = df[col][mask].tolist()
    return outliers

def detect_bool_outliers(df):
    outliers = {}
    bool_cols = [] #manuel doldur
    for col in bool_cols:
        invalid_values = df[~df[col].isin([True, False])]  # True veya False olmayanları bul
        if not invalid_values.empty:
            outliers[col] = invalid_values  # Aykırıları outliers sözlüğüne ekle
    return outliers


def detect_date_outliers(df):
    outliers = {}
    today = pd.Timestamp.today()  # Şu anki tarih
    date_cols = []
    for col in date_cols:
        invalid_dates = []

        for idx, val in df[col].items():
            if pd.isnull(val):
                continue  # Eksik değerleri atla

            try:
                year = val.year
                month = val.month
                day = val.day

                # Yıl aralığı kontrolü
                if not (2008 <= year <= today.year):
                    invalid_dates.append(idx)
                    continue

                # Tarihin geçerli gün sayısı içinde olup olmadığını kontrol et
                try:
                    pd.Timestamp(year=year, month=month, day=day)
                except ValueError:
                    invalid_dates.append(idx)

            except Exception:
                invalid_dates.append(idx)

        if invalid_dates:
            outliers[col] = df.loc[invalid_dates]

    return outliers

def save_all_outliers(df, out_json_path="all_outliers.json", min_freq_ratio=0.01):
    out = {
        "numeric_outliers": {},
        "categorical_outliers": {},
        "bool_outliers": {},
        "date_outliers": {},
    }

    #  Sayısal aykırılar 
    numeric_outs = detect_numeric_outliers(df)  # numeric_cols manuel olarak dolu olacak
    for col, vals in numeric_outs.items():
        out["numeric_outliers"][col] = vals  # değer veya index listesi

    # Kategorik aykırılar 
    categorical_outs = detect_categorical_outliers(df, min_freq_ratio=min_freq_ratio)  # categoric_cols manuel
    for col, vals in categorical_outs.items():
        out["categorical_outliers"][col] = vals


    #Boolean aykırılar
    bool_outs = detect_bool_outliers(df)  # bool_cols manuel
    for col, rows in bool_outs.items():
        out["bool_outliers"][col] = rows.index.tolist()

    # Tarihsel aykırılar
    date_outs = detect_date_outliers(df)  # date_cols manuel
    for col, rows in date_outs.items():
        out["date_outliers"][col] = rows.index.tolist()

    # JSON’a yaz
    with open(out_json_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=4)

    print(f"✅ 'all_outliers.json' oluşturuldu; aykırılar dahil edildi.")
