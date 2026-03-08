def prepare_time_series(df, json_path="veri_temiz.json"):

    manuel_zaman_serisi = []         #manuel doldur
    
    for col in manuel_zaman_serisi:
        df[col] = pd.to_datetime(df[col])
        df.set_index(col, inplace=True)  

    df.sort_index(inplace=True)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=4)

    print(f"✅ İstenilen Sutünlar zaman serisi formatına çevirildi ve '{json_path}' dosyası güncellendi.")

   


    
