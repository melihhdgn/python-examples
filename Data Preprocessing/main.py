import pandas as pd
import numpy as np 
import json
from pandas import json_normalize
from chart import goster_grafikler
from fill_Edit import (
    fix_numeric_type_mismatches,
    fix_text_type_mismatches,
    fill_numeric_nulls_and_outliers,
    fill_categorical_outliers_with_mode,
    fill_bool_nulls_and_outliers,
    fill_date_nulls_and_outliers
)
from missing_report import (
    fill_missing_json,
    report_missing,
    save_categorical_columns_to_txt
)
from normalize import normalizes
from outlier_detection import (
    detect_categorical_outliers,
    detect_numeric_outliers,
    detect_bool_outliers,
    detect_date_outliers,
    save_all_outliers
)
from time_series import prepare_time_series

def main():
    """
    temiz_json = fill_missing_json("örnek.json")
    print("✅ Eksik alanlar dolduruldu.")

    # JSON sonrası normalize & cast
    df = pd.json_normalize(json.load(open(temiz_json, encoding="utf-8")))
    df = normalize_and_cast(df)

    print("📊 Sütun tipleri:")
    print(df.dtypes)"""

    #if input("➡️ Eksik veri raporunu görmek ister misiniz? (e/h): ").lower() == "e":
        #report_missing(temiz_json)

    #if input("➡️ str,int,bool ve date sutunları txt'e olarak kaydedelim mi? (e/h): ").lower() == "e":
        #save_categorical_columns_to_txt(df, "kategorik_sutunlar.txt", "numeric_sutunlar.txt","bool_sutunlar.txt","date_sutunlar.txt")

    #if input("➡️ Kategorik aykırı değerleri tespit edelim mi? (e/h): ").lower() == "e":
        #detect_categorical_outliers(df)
"""
    if input("➡️ Sayısal aykırı değerleri tespit edelim mi? (e/h): ").lower() == "e":
        nums = detect_numeric_outliers(df)
        if nums:
            print("🚨 Sayısal sütunlarda aykırı değer indeksleri:")
            for col, idxs in nums.items():
                print(f"→ {col}: {idxs}")
        else:
            print("✅ Sayısal sütunlarda aykırı değer bulunmadı.") """

    #if input("➡️ Bool aykırı değerleri tespit edelim mi? (e/h): ").lower() == "e":
        #detect_bool_outliers(df),
    
    #if input("➡️ Tarihi aykırı değerleri tespit edelim mi? (e/h): ").lower() == "e":
        #detect_date_outliers(df)

    #if input("➡️ Aykırı değerleri JSON'a kaydedelim mi? (e/h): ").lower() == "e":
        #save_all_outliers(df)

    #if input("➡️ Sayısal Tip uyumsuzluklarını düzeltelim mi? (e/h): ").lower() == "e":
        #fix_numeric_columns_using_neighbors
        
     #if input("➡️ Metinsel Tip uyumsuzluklarını düzeltelim mi? (e/h): ").lower() == "e":
        #fix_text_columns_using_neighbors
        
    #if input("➡️ Sayısal boş/aykırı değerleri dolduralım mı? (e/h): ").lower() == "e":
        #fill_numeric_nulls_and_outliers()

    #if input("➡️ Kategorik boş/aykırı değerleri mod ile dolduralım mı? (e/h): ").lower() == "e":
        #fill_categorical_outliers_with_mode()
    
    #if input("➡️ Boolean boş/aykırı değerleri mod ile dolduralım mı? (e/h): ").lower() == "e":
        #fill_bool_nulls_and_outliers()
    
   # if input("➡️ Tarihi boş/aykırı değerleri dolduralım mı? (e/h): ").lower() == "e":
        #fill_date_nulls_and_outliers()
        
    #if input("➡️ Veri analizi için grafik istermisin ?  (e/h): ").lower() == "e":   
        #goster_grafikler()

    # if input("➡️ Veriyi zaman serisi haline getirelim mi? (e/h): ").lower() == "e":
        #prepare_time_series()
       
    #if input ("➡️ Verileri ölçeklendirmek için normalize yapmak istermisiniz? (e/h)").lower() == "e":
        #normalize(df, "veri_temiz.json")
        #print("✅ Veriler normalize edildi ve 'veri_normalize.json' olarak kaydedildi.")

if __name__ == "__main__":
    main()
