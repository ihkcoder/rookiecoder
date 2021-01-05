"""
*** "if"ifadesinin içerisinde verilen koşul doğru (true) ise çalışır. 

*** Birden fazla koşulun olduğu durumlarda "elif" kullanmamız gerekir.

*** "elif" deyimi if deyimi ile birlikte kullanılır
if deyiminin sağlamadığı diğer koşulu kontrol eder.


***Bu deyim if ve elif ifadelerinin koşulu sağlayamadığı durum da çalışır.
Yani hem if hemde elif koşullarının sağlanmaması durumunda else bloğu devreye girer.

"""

dolarDun = 7.45
dolarBugun = 7.35

if   dolarDun>dolarBugun :               
           print("Dolar düşüyor")
           

elif dolarDun<dolarBugun :
           print ("Dolar artıyor")
                 

else:
          print("Dolar sabit")

print("İşlem Sonu")
