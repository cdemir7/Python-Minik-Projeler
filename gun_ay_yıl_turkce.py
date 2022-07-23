from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL,'')

def tarihFormati(tarih):
    return  datetime.strftime(tarih,'%d %B %Y %X')

bugun = datetime.now()
print(tarihFormati(bugun))
