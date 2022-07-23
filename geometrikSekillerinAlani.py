import math

def UcgenAlan(taban,yukseklik):
    alan = taban * yukseklik / 2
    print("Üçgenin Alanı: ",alan)

def KareAlan(kenar):
    alan = kenar * kenar
    print("Karenin Alanı: ",alan)

def DikdortgenAlan(uzunK,kısaK):
    alan = kısaK * uzunK
    print("Dikdörgetnin Alanı: ",alan)

def DaireAlan(pi,yaricap):
    alan = pi * yaricap * yaricap
    print("Dairenin Alanı: ",alan)

def BesgenAlan(cevre,yukseklik):
    alan = cevre * yukseklik / 2
    print("Besgenin Alanı: ",alan)

def AltigenAlan(kenar):
    alan = ((3 * math.sqrt(3)) * (pow(kenar,2))) / 2
    print("Altıgenin Alanı: ",alan)

while True:
    print("0: Uygulamayı Sonlandır","1: Üçgen","2: Kare","3: Dikdörtgen","4: Daire","5: Beşgen","6: Altıgen", sep='\n')
    secim = input("alanını Öğrenmek İstediğiniz Şekili Giriniz: ")

    if secim == 0:
        break

    elif secim == '1':
        taban = int(input("Taban Değerini Giriniz: "))
        yukseklik = int(input("Yükseklik Değerini Giriniz: "))
        UcgenAlan(taban,yukseklik)

    elif secim == '2':
        kenar = int(input("Kenar Uzunluğunu Giriniz: "))
        KareAlan(kenar)

    elif secim == '3':
        kısaK = int(input("Kısa Kenar Uzunluğunu Giriniz: "))
        uzunK = int(input("Uzun Kenar Uzunluğunu Giriniz: "))
        DikdortgenAlan(uzunK,kısaK)

    elif secim == '4':
        pi = 3
        yaricap = int(input("Yarıçap Uzunluğunu Giriniz: "))
        DaireAlan(pi,yaricap)

    elif secim == '5':
        cevre = int(input("Çevre Uzunluğunu Giriniz: "))
        yukseklik = int(input("Yükseklik Değerini Giriniz: "))
        BesgenAlan(cevre,yukseklik)

    elif secim == '6':
        kenar = int(input("Kenar Uzunluğunu Giriniz: "))
        AltigenAlan(kenar)

    else:
        print("\n1-6 Arasında Değer Giriniz...\n")

