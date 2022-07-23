def topla(sayi1,sayi2):
    toplam = sayi1 + sayi2
    print("\nToplam: {}\n".format(toplam))

def cikartma(sayi1,sayi2):
    sonuc = sayi1 - sayi2
    print("\nSonuç: {}\n".format(sonuc))

def carpma(sayi1,sayi2):
    sonuc = sayi1 * sayi2
    print("\nSonuç: {}\n".format(sonuc))

def bolme(sayi1,sayi2):
    sonuc = sayi1 / sayi2
    print("\nSonuç: {}\n".format(sonuc))

while True:
    print("1: Toplama")
    print("2: Çıkartma")
    print("3: Çarpma")
    print("4: Bölme")
    
    secim = input("Yapmak İstediğiniz İşlemin Başındaki Rakamı Giriniz(Çıkmak için q'ya basınız): ")
    
    sayi1 = int(input("\nBirinci Sayıyı Giriniz: "))
    sayi2 = int(input("İkinci Sayıyı Giriniz: "))
    
    if   secim == '1':
        topla(sayi1,sayi2)

    elif secim == '2':
        cikartma(sayi1,sayi2)

    elif secim == '3':
        carpma(sayi1,sayi2)

    elif secim == '4':
        bolme(sayi1,sayi2)

    elif secim == 'q':
        break

    else:
        print("Lütfen 1,2,3 ve 4 Sayılarından Bir Tanesini Giriniz...")