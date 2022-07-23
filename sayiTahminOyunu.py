import random

pc_sayi = random.randint(1,20)
tahmin_hakki = 4

while True:
    user_sayi = int(input("1-20 Arasında Bir Sayı Giriniz: "))
    
    if user_sayi == pc_sayi:
        print("Tebrikler Bildiniz :)")
        break
    
    elif user_sayi > pc_sayi:
        print("Tahminim Bu Sayıdan Daha Küçük.")
        tahmin_hakki -= 1
        print("Kalan Tahmin Sayısı: ",tahmin_hakki)

    elif user_sayi < pc_sayi:
        print("Tahminim Bu Sayıdan Daha Büyük.")
        tahmin_hakki -= 1
        print("Kalan Tahmin Sayısı: ",tahmin_hakki)

    if tahmin_hakki == 0:
        print("Tahmin Hakkınız Bitmiştir.")
        print("Bilgisayarın Sonucu: {}".format(pc_sayi))
        break

