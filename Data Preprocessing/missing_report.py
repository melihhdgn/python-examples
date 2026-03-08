import pandas as pd
import numpy as np
import json
from pandas import json_normalize

def fill_missing_json(json_path, output_path="veri_temiz.json"):  #-------> JSON dosyasındaki eksik kolonları bulmak ve doldurmak. 
    def get_nested(row, keys):
        ref = row
        for k in keys:
            if isinstance(ref, dict) and k in ref: #isinstance sözlük olup olmadığını kontrol eder 
                ref = ref[k]
            else:
                return None
        return ref

    with open(json_path, "r", encoding="utf-8") as f:
        contents = json.load(f)

    def extract_all_keys(d, prefix=''):
        keys = []
        for k, v in d.items():
            full_key = f"{prefix}.{k}" if prefix else k  #burası tüm anahtarları düz liste yapar mesel user(city,age(year)) user.city:user.age,user.age.year gibi 
            keys.append(full_key)
            if isinstance(v, dict):
                keys.extend(extract_all_keys(v, full_key))
        return keys

    all_cols = set()
    for row in contents:
        all_cols.update(extract_all_keys(row))  #Elimizde JSON’un tüm olası anahtarlarının düz bir listesi var şuan 
    all_cols = list(all_cols)

    for i, row in enumerate(contents): #boşları doldur
        for col in all_cols:
            keys = col.split('.') #user.city gibileri user,city yapar dizide ama 
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

def report_missing(json_path):  #null olan sutunları raporlama 
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

def save_all_column_types_to_txt(df, path_cat, path_num, path_bool, path_date): 
    # Kategorik (object)
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    with open(path_cat, "w", encoding="utf-8") as f:
        for col in categorical_cols:
            f.write(col + "\n")

    # Sayısal (int, float)
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    with open(path_num, "w", encoding="utf-8") as f:
        for col in numeric_cols:
            f.write(col + "\n")         # -------> int,str,bool ve date sutunlarını txt olarak kaydetme
                                        # neden çünkü hangi sutun nerede onu bilmek manuel dolduracağımız kısmı kolaylaştıracaktır
    # Boolean (True/False)
    bool_cols = df.select_dtypes(include=['bool']).columns.tolist()
    with open(path_bool, "w", encoding="utf-8") as f:
        for col in bool_cols:
            f.write(col + "\n")

    # Tarih/Saat (datetime)
    date_cols = df.select_dtypes(include=['datetime64[ns]', 'datetime']).columns.tolist()
    with open(path_date, "w", encoding="utf-8") as f:
        for col in date_cols:
            f.write(col + "\n")

    print(f"📁 {len(categorical_cols)} kategorik -> {path_cat}")
    print(f"📁 {len(numeric_cols)} sayısal   -> {path_num}")
    print(f"📁 {len(bool_cols)} boolean     -> {path_bool}")
    print(f"📁 {len(date_cols)} tarihsel    -> {path_date}")
