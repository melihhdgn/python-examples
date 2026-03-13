import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def goster_grafikler(json_path="veri_temiz.json"):
    df = pd.read_json(json_path)

    # Fiyat sütunlarını seç (fiyat. ile başlayan tüm sütunlar)
    fiyat_sutunlari = [col for col in df.columns if col.startswith("fiyat.")]
    # Fiyatları birleştir (tek seri haline getir)
    fiyatlar = pd.concat([df[col].dropna() for col in fiyat_sutunlari], ignore_index=True)

    # Grafik 1: Fiyat dağılımı (tüm fiyatlar)
    plt.figure(figsize=(10,6))
    sns.histplot(fiyatlar, bins=30, kde=True)
    plt.title("Tüm Fiyatların Dağılımı")
    plt.xlabel("Fiyat")
    plt.ylabel("Frekans")
    plt.savefig("fiyat_dagilimi.jpg")
    plt.close()

    # Grafik 2: Çeşitlere göre fiyat dağılımı
    # Burada ise fiyatlar sütunlarını uzun formata çevirmek lazım.
    # Örneğin melt ile 'çeşit' ve tüm fiyat sütunlarını birleştir
    if fiyat_sutunlari:
        fiyat_df = df[['çeşit'] + fiyat_sutunlari].melt(id_vars=['çeşit'], value_vars=fiyat_sutunlari, var_name='fiyat_sutunu', value_name='fiyat')
        fiyat_df = fiyat_df.dropna(subset=['fiyat'])

        plt.figure(figsize=(12,6))
        sns.boxplot(x='çeşit', y='fiyat', data=fiyat_df)
        plt.title("Çeşitlere Göre Fiyat Dağılımı")
        plt.xlabel("Çeşit")
        plt.ylabel("Fiyat")
        plt.xticks(rotation=45)
        plt.savefig("cesit_fiyat_boxplot.jpg")
        plt.close()

        # Grafik 3: Yapan’a göre ortalama fiyat
        fiyat_df2 = df[['yapan'] + fiyat_sutunlari].melt(id_vars=['yapan'], value_vars=fiyat_sutunlari, var_name='fiyat_sutunu', value_name='fiyat')
        fiyat_df2 = fiyat_df2.dropna(subset=['fiyat'])

        plt.figure(figsize=(12,6))
        sns.barplot(x='yapan', y='fiyat', data=fiyat_df2, estimator=np.mean)
        plt.title("Ustalara Göre Ortalama Fiyat")
        plt.xlabel("Yapan")
        plt.ylabel("Ortalama Fiyat")
        plt.xticks(rotation=45)
        plt.savefig("yapan_ortalama_fiyat.jpg")
        plt.close()

    # Grafik 4: Yer bazında ürün sayısı
    if 'yer' in df.columns:
        plt.figure(figsize=(10,6))
        sns.countplot(x='yer', data=df)
        plt.title("Şehirlere Göre Ürün Sayısı")
        plt.xlabel("Yer")
        plt.ylabel("Ürün Sayısı")
        plt.xticks(rotation=45)
        plt.savefig("yer_urun_sayisi.jpg")
        plt.close()

    # Grafik 5: Eksik veri haritası
    plt.figure(figsize=(12,6))
    sns.heatmap(df.isnull(), cbar=False, cmap='coolwarm')
    plt.title("Eksik Veri Haritası")
    plt.savefig("eksik_veri_haritasi.jpg")
    plt.close()

    print("✅ Grafikler jpg olarak kaydedildi.")
