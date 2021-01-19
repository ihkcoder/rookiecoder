"""
* İngilizce bir kelime olan while, Türkçede ‘… iken, … olduğu sürece’ gibi anlamlara gelir. 

** "while" Yazdığımız kodları tekrar çalıştırmamızı sağlayan döngü çeşididir. 
Çalışma mantığı ise while döngüsü her defasında tekrarlanır , eğer koşul sağlıyorsa
tekrar döngüye girer, eğer sağlamıyorsa döngü sonlanır.

*** "while" döngüleri, bir mantıksal şart mantıksal “doğru” değerine sahip olduğu sürece
tekrarlanır. Döngünün sona ermesi için şartın eninde sonunda yanlış hale gelmesi gerekir

**** Döngünün içinde değişkenler uygun şekilde güncellenir. Güncellemeyi
unutursak sonsuz döngü içine düşeriz ve programımız biz zorla kapatmadıkça durmaz.
ÖRNEK 1'E BAK !!!

***** while True ifadesi şöyle bir anlama gelir: True olduğu müddetçe…

"""

#-------------------------While-------------------------#
"""
#ÖRNEK 1  
a = 1                         # BU ŞEKİLDE SONSUZ DÖNGÜYE GİRER !
                                   
while a == 1:
     print("ERROR !!!")       # Çıkmak için CTRL + C'yi kullanmanız gerekir.
"""     

sayi = 0

while sayi <= 10:
    sayi += 1
    print(sayi)


while True:
 
     vize = int(input("Vize Notu :"))
 
     final = int(input("Final Notu :"))
     ortalama = (vize * 0.4) + (final * 0.6)  # vizenin %40 final %60 olarak alındı
 
     if (ortalama >= 85):
 
          print("Harf notunuz : AA0")
 
     elif (ortalama >= 70 and ortalama < 85):
 
          print("Harf notunuz : BA")
 
     elif (ortalama >= 60 and ortalama < 70):
 
          print("Harf notunuz : BB")
 
     elif (ortalama >= 45 and ortalama < 60):
 
          print("Harf notunuz : CB")
 
     elif (ortalama >= 0 and ortalama < 45):
 
          print("Harf notunuz : FF")
     break
