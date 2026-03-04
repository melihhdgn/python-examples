"""
Kullanıcıdan sürekli tam sayı al.

Program şu şekilde çalışsın:

Kullanıcı aynı sayıyı ikinci kez girdiği anda program dursun.

Program durduğunda:

Girilen benzersiz sayıların listesini yazdır

Girilen sayıların:

artan sırada hâlini yazdır

Girilen sayılar içinde:

en büyük ve en küçük sayıyı yazdır

Girilen sayıların ortalamasını yazdır
(ortalama = toplam / adet)


"""
"""
def number_similarity(numbers, number):
    for x in numbers[:-1]:   # son eklenen hariç kontrol
        if number == x:
            return False
    return True


def numbers_average(numbers):
    toplam = 0
    for i in numbers:
        toplam += i
    if len(numbers) == 0:
        return 0
    return toplam / len(numbers)


def numbers_list(numbers):
    for i in numbers:
        print(i)


def numbers_max(numbers):
    max_sayi = numbers[0]
    for i in numbers:
        if i > max_sayi:
            max_sayi = i
    return max_sayi


def numbers_min(numbers):
    min_sayi = numbers[0]
    for i in numbers:
        if i < min_sayi:
            min_sayi = i
    return min_sayi


def increasing_numbers(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


numbers = []

while True:
    number = int(input("Bir sayı giriniz: "))
    numbers.append(number)

    if len(numbers) >= 2 and not number_similarity(numbers, number):
        print("\nGirilen benzersiz sayılar:")
        numbers_list(numbers[:-1])   # tekrar girilen sayıyı dahil etme

        print(f"\nOrtalama: {numbers_average(numbers[:-1])}")
        print(f"Maksimum: {numbers_max(numbers[:-1])}")
        print(f"Minimum: {numbers_min(numbers[:-1])}")
        print(f"Sıralı hali: {increasing_numbers(numbers[:-1])}")
        break
""""""

# buda bu kodun kısaltılmış hali 
numbers = []

while True:
    n = int(input("Bir sayı giriniz: "))

    if n in numbers:
        break

    numbers.append(n)

print("\nGirilen benzersiz sayılar:", numbers)

print("Sıralı hali:", sorted(numbers))
print("Maksimum:", max(numbers))
print("Minimum:", min(numbers))
print("Ortalama:", sum(numbers) / len(numbers))

"""



numbers = []

while True:
    n = int(input("Bir sayı giriniz: "))
    if n in numbers:
        break
    numbers.append(n)

print("Girilen benzersiz sayılar:", numbers)
print("Girilen sayıların içindeki max:", max(numbers))
print("Girilen sayıların içindeki min:", min(numbers))
print("Girilen sayıların ortalaması:", sum(numbers)/len(numbers))
print("Girilen sayıların sıralaması:", sorted(numbers))
