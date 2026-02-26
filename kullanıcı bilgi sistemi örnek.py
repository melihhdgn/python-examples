import re

kisiler = {}  # Kullanıcıları saklayacak sözlük

def password_check():
    """Şifreyi kontrol eden fonksiyon"""
    while True:
        password = input("Şifrenizi giriniz \n(en az 1 büyük harf, 1 küçük harf ve 1 özel karakter içermelidir): ")
        if (re.search(r'[A-Z]', password) and  
            re.search(r'[a-z]', password) and  
            re.search(r'[\W_]', password)):    
            print("Şifre kabul edildi.\n")
            return password 
        else:
            print("Şifre kurallara uymuyor! Lütfen tekrar deneyin.")

def sign_up():
    """Yeni kullanıcı kaydı oluşturur"""
    while True:
        user_name = input('Kullanıcı adı giriniz: ')
        if user_name in kisiler:
            print("Bu kullanıcı adı zaten alınmış! Lütfen farklı bir isim deneyin.")
        else:
            break
    
    email = input('E-posta adresinizi giriniz: ')
    password = password_check()
    
    kisiler[user_name] = {'kullanici_adi': user_name, 'eposta': email, 'sifre': password}
    print(f"Kullanıcı {user_name} başarıyla oluşturuldu!\n")

def login():
    """Kullanıcı girişi yapar"""
    user_name = input('Kullanıcı adınızı giriniz: ')
    if user_name not in kisiler:
        print("Böyle bir kullanıcı bulunamadı! Lütfen önce kayıt olun.\n")
        return None
    
    password = input('Şifrenizi giriniz: ')
    if kisiler[user_name]['sifre'] == password:
        print(f"\nHoş geldiniz {user_name}!\n")
        return user_name
    else:
        print("Hatalı şifre! Lütfen tekrar deneyin.\n")
        return None

def list_users():
    """Tüm kullanıcıları listeler"""
    if not kisiler:
        print("Sistemde kayıtlı kullanıcı bulunmamaktadır.")
    else:
        print("\nKayıtlı Kullanıcılar:")
        for user, info in kisiler.items():
            print(f"Kullanıcı Adı: {info['kullanici_adi']}, E-posta: {info['eposta']}")
    print()

def delete_user():
    """Kullanıcı silme işlemi"""
    user_name = input("Silmek istediğiniz kullanıcı adı: ")
    if user_name in kisiler:
        del kisiler[user_name]
        print(f"{user_name} başarıyla silindi!\n")
    else:
        print("Böyle bir kullanıcı bulunamadı!\n")

def update_user():
    """Kullanıcı bilgilerini günceller"""
    user_name = input("Güncellemek istediğiniz kullanıcı adı: ")
    if user_name in kisiler:
        print("Güncellemek istediğiniz alanı seçin:\n1. Kullanıcı Adı\n2. E-posta\n3. Şifre")
        secim = input("Seçiminiz: ")
        
        if secim == "1":
            new_name = input("Yeni kullanıcı adınızı girin: ")
            kisiler[new_name] = kisiler.pop(user_name)
            kisiler[new_name]['kullanici_adi'] = new_name
            print("Kullanıcı adı başarıyla güncellendi!\n")
        
        elif secim == "2":
            new_email = input("Yeni e-posta adresinizi girin: ")
            kisiler[user_name]['eposta'] = new_email
            print("E-posta başarıyla güncellendi!\n")
        
        elif secim == "3":
            new_password = password_check()
            kisiler[user_name]['sifre'] = new_password
            print("Şifre başarıyla güncellendi!\n")
        
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.\n")
    else:
        print("Böyle bir kullanıcı bulunamadı!\n")

# Sonsuz Döngü ile Kullanıcı Seçimi
while True:
    try:
        secim = input('''\nYapmak istediğiniz işlemi seçin:
1 - Kayıt Ol
2 - Giriş Yap
3 - Kullanıcıları Listele
4 - Kullanıcı Sil
5 - Kullanıcı Güncelle
6 - Çıkış
Seçiminiz: ''')

        if secim == "1":
            sign_up()
        elif secim == "2":
            aktif_kullanici = login()
        elif secim == "3":
            list_users()
        elif secim == "4":
            delete_user()
        elif secim == "5":
            update_user()
        elif secim == "6":
            print("Sistemden çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-6 arasında bir rakam girin.")
    
    except Exception as e:
        print(f"Bir hata oluştu: {e}")