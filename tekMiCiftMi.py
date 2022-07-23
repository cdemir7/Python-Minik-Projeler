while True:
    metin = "Lütfen Bir Sayı Giriniz..."
    try:
        sayi = int(input("Lütfen Bir Sayı Giriniz: "))
        if sayi % 2 == 1:
            print("{} Tek Sayıdır.".format(sayi))

        elif(sayi % 2 == 0):
            print("{} Çift Sayıdır.".format(sayi))
    except ValueError :
        print("Hata: {}".format(metin))
        quit()