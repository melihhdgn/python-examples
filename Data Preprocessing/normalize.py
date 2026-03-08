def normalizes(df, outpath):
    scale_columns = ["fiyat.24", "fiyat.25", "fiyat.26"] #manuel doldurssss
    scaler = MinMaxScaler()  #hazır fonk 
    for col in scale_columns:
        df[[col]] = scaler.fit_transform(df[[col]])
    df.to_json(outpath, orient="records", force_ascii=False)