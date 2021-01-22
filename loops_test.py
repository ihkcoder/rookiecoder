#-------------------------Test-------------------------#
"""
1- Sayilar listesini while ile ekrana yazdırınız.
"""
sayilar = [1,3,5,7,9,12,19,21]

i = 0
while (i < len(sayilar)):
     print(sayilar[i])
     i += 1

"""
2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki
tüm tek sayıları ekrana yazdırınız.
"""

baslangic = int(input('başlangıç: '))
bitis = int(input('bitiş: '))

i = baslangic

while i < bitis:
     i += 1
     if (i % 2 == 1):
          print(i)
