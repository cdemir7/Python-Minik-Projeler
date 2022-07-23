import random as rd

secenekler = ['taş', 'kağıt', 'makas']
tas = secenekler[0]
kagit = secenekler[1]
makas = secenekler[2]

print("Taş kağıt makas oyununa hoşgeldiniz.....")
print("Oyundan çıkmak için e tuşuna basınız....")

while True:
    secim = input("Taş mı? Kağıt mı? Makas mı?: ")
    bil_secim = rd.choice(secenekler)
    if secim == 'taş':
        if bil_secim == tas:
            print("Bilgisayarın Seçimi: Taş")
            print("Sonuç: Berabere")
            print("Hadi yine iyisin bu sefer kurtuldun :)")
        elif bil_secim == kagit:
            print("Bilgisayarın Seçimi: Kağıt")
            print("Sonuç: Kaybettin")
            print("Ben sana kazanamayacağını söylemiştim :)))")
        else:
            print("Bilgisayarın Seçimi: Makas")
            print("Sonuç: Kazandın")
            print("Bu sefer sana gününü göstericem :(((")

    if secim == 'kağıt':
        if bil_secim == tas:
            print("Bilgisayarın Seçimi: Taş")
            print("Sonuç: Kazandın")
            print("Bu sefer sana gününü göstericem :(((")
        elif bil_secim == kagit:
            print("Bilgisayarın Seçimi: Kağıt")
            print("Sonuç: Berabere")
            print("Hadi yine iyisin bu sefer kurtuldun :)")
        else:
            print("Bilgisayarın Seçimi: Makas")
            print("Sonuç: Kaybettin")
            print("Ben sana kazanamayacağını söylemiştim :)))")

    if secim == 'makas':
        if bil_secim == tas:
            print("Bilgisayarın Seçimi: Taş")
            print("Sonuç: Kaybettin")
            print("Ben sana kazanamayacağını söylemiştim :)))")
        elif bil_secim == kagit:
            print("Bilgisayarın Seçimi: Kağıt")
            print("Sonuç: Kazandın")
            print("Bu sefer sana gününü göstericem :(((")
        else:
            print("Bilgisayarın Seçimi: Makas")
            print("Sonuç: Berabere")
            print("Hadi yine iyisin bu sefer kurtuldun :)")

    if secim == 'e':
        print("Oyun Sonlandırılıyor....")
        break