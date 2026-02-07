register = []
tek = []
cift = []

for i in range(0,5):
    x = int(input(f"{i}.sayıyı giriniz."))
    register.append(x)

for i in register:
    if i % 2 == 0:
        cift.append(i)
    else:
        tek.append(i)

while True:
    reply = input("Yapmak istediğiniz işlem ne?\n" 
    "1.Çift mi Tek mi kontrölü ?\n" 
    "2.Kaç tane çift , kaç tane tek sayı olduğu\n" 
    "3.Çİft sayıların toplamı\n" 
    "4.Tek sayıların Toplamı\n" 
    "5.Hepsini tek seferde ver.\n"
    "6.Cıkış\n")

    if reply == "1":
        for i in register:
            if i % 2 == 0:
                print(f"{i} sayısı çifttir.")
            else:
                print(f"{i} sayısı tektir.")

    elif reply == "2":
        print(f"{len(cift)} tane çift sayı vardır.")
        print(f"{len(tek)} tane tek sayı vardır.")

    elif reply == "3":
        toplam = 0
        for i in cift:
            toplam = i + toplam
        print(f"Cift sayıların toplamı {toplam} dır.")

    elif reply == "4":
        toplam = 0
        for i in tek:
            toplam = i + toplam
        print(f"Tek sayıların toplamı {toplam} dır.")
    elif reply == "5":
        print("-----OZET-----")
        print(f"Çift sayılar: {cift}")
        print(f"Tek sayılar: {tek}")
        print(f"Çift sayı adedi: {len(cift)}")
        print(f"Tek sayı adedi: {len(tek)}")
        print(f"Çift sayılar toplamı: {sum(cift)}")
        print(f"Tek sayılar toplamı: {sum(tek)}")

    elif reply == "6":
        break
    else :
        print("Lütfen geçerli bir sayı giriniz.(1-6 arasında)")
      


