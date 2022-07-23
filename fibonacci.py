fibonacciDizisi = [0,1]

def elemanGoster(sayi):
    if sayi <= 0:
        print("0 ve 0 dan Küçük Sayı Girilemez")
    
    i = 0
    ilkdeger = 0
    ikincideger = 1
    while i < sayi:
        yenideger = ilkdeger + ikincideger
        ilkdeger = ikincideger
        ikincideger = yenideger
        i += 1
        fibonacciDizisi.append(yenideger)

    

def elemanlariToplami():
    toplam = sum(fibonacciDizisi)
    return toplam

while True:   
    sayi = int(input("Bir Sayı Giriniz: "))
    elemanGoster(sayi)
    print("Fibonacci Dizisini İlk {} Elemanı --> ".format(sayi),fibonacciDizisi)
    print("Fibonacci Dizisinin İlk {} Elemanının Toplamı --> {}".format(sayi,elemanlariToplami()))
    fibonacciDizisi.clear()
    fibonacciDizisi = [0,1]


    