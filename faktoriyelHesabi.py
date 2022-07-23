def faktoriyel(sayi):
    if sayi == 1 or sayi == 0:
        return 1
    else:
        return sayi*faktoriyel(sayi-1)

while True:
    metin = 'Lütfen Pozitif Bir Sayı Giriniz'
    try:
        sayi = int(input("Lütfen Bir Sayı Giriniz: "))
        print("{} Faktöriyeli --> {}".format(sayi,faktoriyel(sayi)))
    except Exception as ex:
        print("Hata: {}".format(metin))