"""
3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre heasaplayınız. 
    
    1. Bakım = 1.yıl 
    2. Bakım = 2.yıl
    3. Bakım = 3.yıl
   
    *** Süre hesabı alınan gün, ay, yıl, bilgisine göre gün bazlı hesaplayınız
    
    *** datetime modülünü kullanmanız gerekiyor.

 bakım1 = trafiğecikis + timedelta.(days = 365) 
 
 bakım2 = trafiğecikis + timedelta.(days = 365) 
 
 bakım3 = trafiğecikis + timedelta.(days = 365) 

"""


import datetime

tarih = (input("Aracınız hangi tarihte trafiğe çıktı (2019/8/9): "))

tarih = tarih.split("/")

# print(tarih[0])
# print(tarih[1])
# print(tarih[2])


trafıgecikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

simdi = datetime.datetime.now()

fark = simdi - trafıgecikis

days = fark.days

if days <= 365 :
     print("1.servis aralığı")

elif days > 365  and days <= 365*2 :
     print("2.servis aralığı")

elif days > 365*2  and days <= 365*3 :
     print("3.servis aralığı")

else:
    print("hatalı bilgi")
