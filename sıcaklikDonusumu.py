def celtoFah():
    deger = int(input("\nDeğeri Giriniz: "))
    sonuc = (deger * 1.8) + 32
    print("\n{} Celsius = {} Fahrenheit \n".format(deger,sonuc))

def fahtoCel():
    deger = int(input("\nDeğeri Giriniz: "))
    sonuc = (deger - 32) / 1.8
    print("\n{} Fahrenheit = {} Celsius \n".format(deger,sonuc))

def celtoKel():
    deger = int(input("\nDeğeri Giriniz: "))
    sonuc = deger + 273.15
    print("\n{} Celsius = {} Kelvin \n".format(deger,sonuc))

def keltoCel():
    deger = int(input("\nDeğeri Giriniz: "))
    sonuc = deger - 273.15
    print("\n{} Kelvin = {} Celsius \n".format(deger,sonuc))


while True:
    print("*********************************************")
    print("Sıcaklık Dönüşümü Uygulamasına Hoşgeldiniz")
    print("*********************************************\n")
    print("1: Celsius    --> Fahrenheit")
    print("2: Fahrenheit --> Celsius")
    print("3: Celsius    --> Kelvin")
    print("4: Kelvin     --> Celsius")
    secim = input("\nYapmak İstediğiniz İşlemi Giriniz(Çıkış için q'ya basınız): ")

    if secim == '1':
        celtoFah()
    elif secim == '2':
        fahtoCel()
    elif secim == '3':
        celtoKel()
    elif secim == '4':
        keltoCel()
    elif secim == 'q':
        break
    else:
        print("Yanlış bir değer girdiniz")
        print("Tekrar Deneyin...")