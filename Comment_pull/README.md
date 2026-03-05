# Comment Puller - iOS & Android Yorum Çekme

Bu proje, iOS ve Android uygulamalarının kullanıcı yorumlarını çekmek için hazırlanmış genel bir Python örnek kodudur.  

> Not: Bu kod herhangi bir sektöre özel değildir, istediğiniz uygulamaların yorumlarını çekebilirsiniz.

---

## 📂 Dosya

- `comment_pull.py` : iOS ve Android yorumlarını çeken ana Python dosyası.
- `sarj_firma_yorumlari_karisik.xlsx` : Örnek çıktı (çalıştırdığınızda oluşur).

---

## ⚙️ Kurulum

1. Python 3.9 veya üstünü yükleyin.
2. Gerekli paketleri yükleyin:

```bash
pip install requests pandas google_play_scraper openpyxl

📝 Kullanım

comment_pull.py dosyasını açın.

apps değişkenine yorumlarını çekmek istediğiniz uygulamaları ekleyin. Örnek:

apps = [
    {"name": "BINBIN", "ios": 1483635924, "android": "com.BINBIN"},
    {"name": "Diğer Uygulama", "ios": 1234567890, "android": "com.ornek.uygulama"}
]

iOS ve Android ID’lerini aşağıdaki şekilde bulabilirsiniz:

📱 iOS App Store ID Bulma

App Store’da uygulamanın sayfasına gidin.

URL’de id ile başlayan numara uygulamanın iOS ID’sidir:

https://apps.apple.com/tr/app/binbin/id1483635924
                                    ↑↑↑

Bu örnekte iOS ID = 1483635924.

🤖 Google Play Store ID Bulma

Google Play’de uygulamanın sayfasına gidin.
Paylaş'a basın.
URL’de id parametresi Android paketi adıdır:

https://play.google.com/store/apps/details?id=com.BINBIN&hl=tr&gl=TR
                                    ↑↑↑

Bu örnekte Android ID = com.BINBIN.

⚡ Öneriler

iOS için count parametresi genellikle 50–100 arası tutulmalı.

Android için count parametresi 200’e kadar güvenli.

Daha fazla yorum çekmek istiyorsanız kodu sayfa bazlı döngü ile güncelleyebilirsiniz.
