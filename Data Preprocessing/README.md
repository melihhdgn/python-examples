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
