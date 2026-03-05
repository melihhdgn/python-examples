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

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

This project is a simple Python example for extracting user reviews from iOS App Store and Google Play Store.

Note: This script is not tied to any specific industry. You can use it to collect reviews from any mobile application.

📂 Files

comment_pull.py : Main Python script that fetches iOS and Android reviews.

sarj_firma_yorumlari_karisik.xlsx : Example output file (generated after running the script).

⚙️ Installation

Install Python 3.9 or higher.

Install required packages:

pip install requests pandas google_play_scraper openpyxl
📝 Usage

Open the comment_pull.py file.

Add the applications you want to analyze inside the apps variable.

Example:

apps = [
    {"name": "BINBIN", "ios": 1483635924, "android": "com.BINBIN"},
    {"name": "Another App", "ios": 1234567890, "android": "com.example.app"}
]

Run the script:

python comment_pull.py

After running the script, an Excel file containing all collected reviews will be created.

📱 How to Find App IDs
iOS App Store ID

Open the application page on the App Store.

Look at the number that comes after id in the URL.

Example:

https://apps.apple.com/tr/app/binbin/id1483635924
                                    ↑

In this example:

iOS ID = 1483635924
🤖 Google Play Store Package ID

Open the application page on Google Play.

Click Share.

The id parameter in the URL is the Android package name.

Example:

https://play.google.com/store/apps/details?id=com.BINBIN&hl=tr&gl=TR
                                             ↑

In this example:

Android ID = com.BINBIN
⚡ Recommendations

For iOS, keeping the count parameter between 50–100 is recommended.

For Android, the count parameter can safely go up to 200.

If you want to collect more reviews, you can modify the script to use pagination loops.
