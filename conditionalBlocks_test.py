"""
*f-stringlerin genel amamcı string içinde 
python ifadeleri yazabilme olanağı sağlamasıdır.

**f-string karekter dizelerini biçimlendirmeye yarar.

***f-string Diğer biçimlendirme yöntemlerine göre yalnızca daha okunaklı, 
daha özlü ve hata yapmaya daha az eğilimli olmakla kalmazlar, 
aynı zamanda daha hızlıdırlar!

****ÖRNEK Kod:
isim = 'İsmail'
string = f"Merhabalar {isim}"
print(string)

Out
Merhabalar İsmail

DİKKAT: f-string yapısı Python 3.6 sürümü ile birlikte eklendi. 
"""
# (Soru) Girilen üç sayıyı büyüklük olarak karşılaştırınız.

sayi1  = int(input("1.Sayıyı gir : "))

sayi2  = int(input("2.Sayıyı gir : "))

sayi3  = int(input("3.Sayıyı gir : "))

if (sayi1 > sayi2) and (sayi1 > sayi3): 
     print (f"{sayi1} sayisı en büyük sayıdır") 


elif (sayi2 > sayi1) and (sayi2 > sayi3):
     print (f"{sayi2} sayisı en büyük sayıdır")  


else:
     print (f"{sayi3} sayisı en büyük sayıdır") 
