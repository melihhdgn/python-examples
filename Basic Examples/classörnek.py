class Student:
    def __init__(self):
        self.ad_soyad_not = {"Melih Dogan": 50, "Ebubekir Eker": 60, "Yusuf Azad": 70}
       
    def not_ekle(self, isim, soyisim, puan):
        tam_isim = f"{isim} {soyisim}"
        if tam_isim in self.ad_soyad_not:
            self.ad_soyad_not[tam_isim] += puan
            print(f"{tam_isim} adlı öğrencinin yeni puanı: {self.ad_soyad_not[tam_isim]}")
        else:
            self.ad_soyad_not[tam_isim] = puan
            print(f"Yeni öğrenci eklendi: {tam_isim} - Puan: {puan}")

    def notlari_goster(self):
        print("\nÖğrenci Notları:")
        for ogrenci, puan in self.ad_soyad_not.items():
            print(f"{ogrenci}: {puan}")

# Kullanım örneği (class dışında olmalı)
if __name__ == "__main__":
    ogrenci = Student()
    ogrenci.notlari_goster()

    print("\nNot Ekleme Örnekleri:")
    ogrenci.not_ekle("Melih", "Dogan", 20)  # Var olan öğrenci
    ogrenci.not_ekle("Ayşe", "Yılmaz", 90)  # Yeni öğrenci

    ogrenci.notlari_goster()