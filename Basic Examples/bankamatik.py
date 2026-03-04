def bankamatik():
    # Hesaplar
    MelihHesap = {
        'ad': 'Melih Doğan',
        'Hesap_no': '459145',
        'bakiye': 5000,
        'ek_hesap': 3000
    }

    EfeHesap = {
        'ad': 'Efe Elibol',
        'Hesap_no': '451945',
        'bakiye': 3000,
        'ek_hesap': 4000
    }

    # Kullanıcıdan hangi hesapla işlem yapacağını sor
    hesap_secimi = input("Hangi hesapla işlem yapmak istersiniz? (Melih/Efe): ").lower()

    # Seçilen hesaba göre işlem yapma
    if hesap_secimi == "melih":
        hesap = MelihHesap
    elif hesap_secimi == "efe":
        hesap = EfeHesap
    else:
        print("Geçersiz seçim, işlem sonlandırılıyor.")
        return

    # Sonsuz döngü ile işlem menüsü
    while True:
        print("""\n1-Para çekme
2-Para yatırma
3-Bakiye bilgisi öğrenme
4-Çıkış""")
        try:
            selection = int(input("Hangi işlemi yapmak istersiniz:"))
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")
            continue
        
        match selection:
            case 1:  # Para çekme işlemi
                withdrawal = int(input("Çekmek istediğiniz bakiye nedir: "))
                if withdrawal <= hesap['bakiye']:
                    hesap['bakiye'] -= withdrawal  # Bakiye çekme
                    print(f"İyi günler, yeni bakiye = {hesap['bakiye']}")
                elif withdrawal > hesap['bakiye']:
                    additional_withdrawal = input('Yetersiz bakiye, ek hesaptan çekmek ister misiniz? (evet/hayır): ').lower()
                    match additional_withdrawal:
                        case "evet":
                            total_balance = hesap['bakiye'] + hesap['ek_hesap']
                            if withdrawal <= total_balance:
                                if withdrawal <= hesap['bakiye']:
                                    hesap['bakiye'] -= withdrawal
                                else:
                                    hesap['ek_hesap'] -= (withdrawal - hesap['bakiye'])
                                    hesap['bakiye'] = 0  # Ana bakiye sıfırlanır
                                print(f"İyi günler, yeni bakiye = {hesap['bakiye']}, Ek hesap = {hesap['ek_hesap']}")
                            else:
                                print("Yetersiz bakiye, işleminizi gerçekleştiremiyorum.")
                        case "hayır":
                            print("İşlem iptal edildi.")
            case 2:  # Para yatırma işlemi
                deposit = int(input("Yatırmak istediğiniz para miktarı nedir: "))
                hesap['bakiye'] += deposit
                print(f"Yeni bakiye: {hesap['bakiye']}")
            case 3:  # Bakiye bilgisi
                print(f"Ad-Soyad: {hesap['ad']}")
                print(f"Bakiye: {hesap['bakiye']}")
                print(f"Ek Hesap: {hesap['ek_hesap']}")
                print(f"Hesap No: {hesap['Hesap_no']}")
            case 4:  # Çıkış
                print("Çıkış yapılıyor...")
                return  # Fonksiyonu sonlandırır
            case _:  # Geçersiz seçenek
                print("Geçersiz işlem numarası, lütfen tekrar deneyin.")

# Bankamatik fonksiyonunu çağır
bankamatik()
