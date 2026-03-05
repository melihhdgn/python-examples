📊 Data Preprocessing Pipeline

Bu proje, büyük ölçekli veri setlerini modele vermeden önce temizlemek ve analiz için hazır hale getirmek amacıyla geliştirilmiş modüler bir veri ön işleme pipeline yapısıdır.

🔎 Neler Yapıyor?

Eksik (null) veri tespiti ve raporlama

Aykırı değer (outlier) analizi ve JSON olarak kayıt

Tip uyumsuzluklarını düzeltme

Boş ve aykırı değerleri kontrollü doldurma

Zaman serisi formatına dönüştürme

Min-Max normalize (0–1 ölçekleme)

Analiz için grafik altyapısı

⚙️ Tasarım Yaklaşımı

Modüler yapı (her adım bağımsız çalıştırılabilir)

Büyük veri odaklı tasarım (1M+ / 100M+ satır senaryosu)

Gereksiz işlem yükünü azaltmaya yönelik kontrol mekanizması

Performans optimizasyonuna açık mimari

🎯 Amaç

Ham veriyi → temiz, tutarlı ve model-ready hale getirmek.
------------------------------------
📊 Data Preprocessing Pipeline

This project provides a modular data preprocessing pipeline designed to clean and prepare large-scale datasets before they are used for analysis or machine learning models.

🔎 Features

Detection and reporting of missing (null) values

Outlier analysis with results saved as JSON

Data type correction for inconsistent columns

Controlled filling of missing and abnormal values

Conversion to time series format

Min-Max normalization (0–1 scaling)

Basic visualization support for data analysis

⚙️ Design Approach

Modular structure (each step can run independently)

Designed for large datasets (1M+ / 100M+ rows)

Built-in checks to avoid unnecessary processing

Architecture that allows performance optimization and scalability

🎯 Purpose

Transform raw data → clean, consistent, and model-ready datasets suitable for analytics and machine learning workflows.
