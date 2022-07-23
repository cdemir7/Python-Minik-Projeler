sayi = int(input("Bir sayı giriniz: "))
toplam = 0
gecici = sayi

while gecici > 0:
    digit = gecici % 10
    toplam += (digit ** 3)
    gecici //= 10


if sayi == toplam:
    print("{} Armstrong sayısıdır.".format(sayi))
else:
    print("{} Armstrong sayısıdır.".format(sayi))
