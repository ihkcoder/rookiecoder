"""
1- Kullanıcıdan isim yaş ve eğitim bilgileri isteyip ehliyet alabilme
   durumunu kontrol ediniz. Ehliyet alma kursunun en az 18 yaş ve eğitim durumu
   lise ya da üniversite olmalıdır.
"""
isim = input("isminiz: ")
yas = int(input("yaşınız: "))
egitim = input("eğitim: ")


if (yas >= 18):
     if egitim == "üniversite" or egitim == "lise":
          print(f"{isim} bey ehliyet alabilirsiniz")
     else:
          print(f"{isim} bey ehliyet alamazsınız eğitim durumunuz yetersiz")     

else :
     print(f"{isim} bey ehliyet alamazsınız yaşınız tutmuyor ")

"""
2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp  hesaplanan ortalamaya göre
   not aralığına karşılık gelen not bilgisini yazdırınız.

0 -24 = 0
25-44 => 1
45-54 => 2
55-69 => 3
70-84 => 4
85-100 => 5
"""
yazili1 = float(input("1.yazılı: "))
yazili2 = float(input("2.yazılı: "))
sozlu = float(input("sözlü: "))

ortalama = (yazili1 + yazili2 + sozlu)/3

if ortalama >= 0 and ortalama <= 24 :
     print(f"Not Ortalamanız :{ortalama} puanınız :0")   

elif  ortalama >= 25 and ortalama <= 44 :  
     print(f"Ortalamanız :{ortalama} Notunuz :1")  

elif  ortalama >= 45 and ortalama <= 54 :  
     print(f"Ortalamanız :{ortalama} Notunuz :2")  

elif  ortalama >= 55 and ortalama <= 69 :  
     print(f"Ortalamanız :{ortalama} Notunuz :3") 

elif  ortalama >= 70 and ortalama <= 84 :  
     print(f"Ortalamanız :{ortalama} Notunuz :4") 

elif  ortalama >= 85 and ortalama <= 100 :  
     print(f"Ortalamanız :{ortalama} Notunuz :5")

else:
     print("Hatalı not girişi!") 
