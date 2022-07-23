import random as rd
import time

kullanici1_skor = 0
kullanici2_skor = 0

while True:
    kullanici1 = rd.randint(1,6)
    time.sleep(0.5)
    kullanici2 = rd.randint(1,6)
    time.sleep(0.5)

    if kullanici1 > kullanici2:
        print("Kullanıcı1 --> {} Kullanıcı2 --> {} Sonuç: Bu Eli Kullanıcı1 Kazandı :)".format(kullanici1,kullanici2))
        kullanici1_skor += 1

    elif kullanici2 > kullanici1:
        print("Kullanıcı1 --> {} Kullanıcı2 --> {} Sonuç: Bu Eli Kullanıcı2 Kazandı :)".format(kullanici1,kullanici2))
        kullanici2_skor += 1

    else:
        print("Kullanıcı1 --> {} Kullanıcı2 --> {} Sonuç: Bu El Berabere :)".format(kullanici1,kullanici2))

    if kullanici1_skor == 5:
        print("\nKullanıcı1 Oyunu Kazandı.")
        print("\nSkor:")
        print("Kullanıcı1: ",kullanici1_skor)
        print("Kullanıcı2: ",kullanici2_skor)
        print()
        break

    elif kullanici2_skor == 5:
        print("\nKullanıcı2 Oyunu Kazandı.")
        print("\nSkor:")
        print("Kullanıcı1: ",kullanici1_skor)
        print("Kullanıcı2: ",kullanici2_skor)
        print()
        break