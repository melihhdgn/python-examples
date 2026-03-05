import requests
import pandas as pd
import time
from google_play_scraper import reviews, Sort

# ======================
# iOS Yorum Çekme Fonksiyonu
# ======================
def get_ios_reviews(app_id, country="tr", count=50):
    all_reviews = []
    
    for page in range(1, (count // 10) + 2):
        url = f"https://itunes.apple.com/{country}/rss/customerreviews/page={page}/id={app_id}/sortby=mostrecent/json"
        
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                print(f"⚠️ iOS Sayfa {page} başarısız (Status: {response.status_code})")
                break
            
            data = response.json()
            feed = data.get('feed', {})
            entries = feed.get('entry', [])
            
            if not entries:
                break
            
            if isinstance(entries, dict):
                entries = [entries]
            
            for i, entry in enumerate(entries):
                # İlk entry uygulama bilgisi, atla
                if i == 0 and 'author' in entry and 'name' in entry['author']:
                    if 'label' in entry['author']['name'] and 'Alıntı Gönder' in entry['author']['name']['label']:
                        continue
                
                if 'author' not in entry or 'content' not in entry:
                    continue
                
                try:
                    review = {
                        "Platform": "iOS",
                        "Firma": "",  # Çağırırken dolduracağız
                        "AppID": app_id,
                        "Kullanıcı": entry.get('author', {}).get('name', {}).get('label', 'Bilinmiyor'),
                        "Puan": int(entry.get('im:rating', {}).get('label', 0)),
                        "Başlık": entry.get('title', {}).get('label', 'Başlık yok'),
                        "Yorum": entry.get('content', {}).get('label', 'Yorum yok'),
                        "Tarih": entry.get('updated', {}).get('label', 'Bilinmiyor')
                    }
                    all_reviews.append(review)
                except:
                    continue
            
            if len(all_reviews) >= count:
                break
            
            time.sleep(1)
            
        except Exception as e:
            print(f"❌ iOS Hata (Sayfa {page}): {e}")
            continue
    
    return all_reviews[:count]

# ======================
# Uygulama Listesi (tek düz liste)
# ======================
apps = [
    {"name": "BINBIN", "ios": 1483635924, "android": "com.BINBIN"},
]

# ======================
# Tüm yorumları çek ve birleştir
# ======================
all_reviews = []

for app in apps:
    company = app["name"]
    ios_id = app.get("ios")
    android_id = app.get("android")
    
    # iOS yorumları
    if ios_id:
        print(f"iOS yorumları çekiliyor: {company}")
        ios_reviews = get_ios_reviews(ios_id, count=50) #EN FAZLA 50 YORUM ÇEK
        for r in ios_reviews:
            r["Firma"] = company
        all_reviews.extend(ios_reviews)
    
    # Android yorumları
    if android_id:
        print(f"Android yorumları çekiliyor: {company}")
        try:
            result, _ = reviews(
                android_id,
                lang="tr",
                country="tr",
                sort=Sort.NEWEST,
                count=200  #EN FAZLA 200 YORUM ÇEK 
            )
            for r in result:
                all_reviews.append({
                    "Platform": "Android",
                    "Firma": company,
                    "AppID": android_id,
                    "Kullanıcı": r["userName"],
                    "Puan": r["score"],
                    "Başlık": "",
                    "Yorum": r["content"],
                    "Tarih": r["at"]
                })
        except Exception as e:
            print(f"Hata Android: {company} -> {e}")

# ======================
# Excel'e yaz
# ======================
df = pd.DataFrame(all_reviews)
df.to_excel("yorumlar_karisik.xlsx", index=False)
print("✅ Tüm yorumlar Excel'e yazıldı.")