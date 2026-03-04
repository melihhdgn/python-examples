ogrenciler = []

while True:
    print("\n--- ÖĞRENCİ NOT SİSTEMİ ---")
    print("1 - Öğrenci ekle")
    print("2 - Öğrencileri listele")
    print("3 - Ortalama hesapla")
    print("4 - Çıkış")

    secim = input("Seçimin: ")

    # 1️⃣ Öğrenci ekleme
    if secim == "1":
        ad = input("Ad: ")
        soyad = input("Soyad: ")

        try:
            notu = float(input("Not (0-100): "))
            if notu < 0 or notu > 100:
                print("Not 0 ile 100 arasında olmalı!")
                continue
        except:
            print("Geçersiz not girdin!")
            continue

        ogrenci = {
            "ad": ad,
            "soyad": soyad,
            "not": notu
        }

        ogrenciler.append(ogrenci)
        print("Öğrenci eklendi ✅")

    # 2️⃣ Listeleme
    elif secim == "4":
        if len(ogrenciler) == 0:
            print("Henüz öğrenci yok!")
        else:
            for i, ogr in enumerate(ogrenciler, start=1):
                print(f"{i}. {ogr['ad']} {ogr['soyad']} - Not: {ogr['not']}")

    # 3️⃣ Ortalama
    elif secim == "3":
        if len(ogrenciler) == 0:
            print("Hesaplanacak öğrenci yok!")
            continue

        toplam = 0
        for ogr in ogrenciler:
            toplam += ogr["not"]

        ortalama = toplam / len(ogrenciler)
        print(f"Ortalama: {ortalama:.2f}")

        if ortalama >= 50:
            print("Durum: Geçti 🎉")
        else:
            print("Durum: Kaldı ❌")

    # 4️⃣ Çıkış
    elif secim == "4":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Hatalı seçim!")
