"""
* Programlama yaparken kullanıcıdan girdi almak oldukça önemlidir.
Pythonda kullanıcıdan girdi almamızı sağlayan fonksiyon input() dur.

** input() fonksiyonu  sadece String(metinsel) 
veri türlerini kullanıcıdan alabiliyoruz.

*** Bu yüzden bir sayı işlemi yapacaksak kullanıcıdan aldığımız (string) değerini 
float ya da int fonksiyonuyla veri tipi dönüştürme işlemi yapmamız gerekir. 

ÖRNEK : isim = input("isminiz: ")          #str
        yas = int(input("yaşınız: "))      #int
        boy = float(input("boyunuz: "))    #float 
   
"""

# Girilen bir sayının 0-100 arasında olup olmadığının kontrol ediniz.

sayi  = int(input("Sayı gir : "))

if  (sayi > 0) and (sayi <= 100):
     print(f"{sayi} sayısı 0-100 arasında bir sayıdır.")

else:
     print(f"{sayi} sayısı 0-100 arasında bir sayı değildir.")
