import math 

def asal_kontrol(n):
        if n<=1:
            return True
        elif n%2==0:
            return False
        for i in range (3, int(math.sqrt(n))+1, 2):
            if n%i==0:
                return False
        return True

def en_kucuk(array2):
    en_kucuk=array2[0]
    for numbers in array2:
        if numbers < en_kucuk:
            en_kucuk = numbers
    return en_kucuk

def en_buyuk(array2):
    en_buyuk=array2[0]
    for numbers in array2:
        if numbers > en_buyuk:
            en_buyuk = numbers  
    return en_buyuk

def ortalama (array2):
    toplam=0
    sayac = 0
    for numbers in array2:
        toplam = toplam + numbers
        sayac+=1
    return toplam/sayac



numbers = input("Aralarında virgül olmak şartı ile sayılar yazınız (en az 9 tane): ")
array = [int(sayi) for sayi in numbers.split(",")]
array2 = []

for sayi in array:
    if asal_kontrol(sayi):
        array2.append(sayi)
        print(f"{sayi} asaldır. Yeni dizi: {array2}")
    

print(f"{en_kucuk(array2)} dizideki en küçük rakam.")
print(f"{en_buyuk(array2)} dizideki en büyük rakam.")
print(f"{ortalama(array2)} dizinin ortalaması.")




    

