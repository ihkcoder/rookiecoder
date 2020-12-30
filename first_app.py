"""
Bir veriyi içerisinde depolayan birime değişken denir.
[Örnek 1'e bak]   

Kelimelerin arası ayrı olması için " " işareti koymamız lazım.
[Örnek 2'e bak]

Program içerinde bir ifadeyi birden çok yerde kullanacaksak bunu bir değişkene atarız.
Çünkü değerini değiştirmek istersek sadece tanımlandığı yeri değiştirmemiz yeterli olur.
[Örnek 3'e bak]

"""
#örnek 1
baslik = "HABERİNİZ OLSUN"     #baslik, vade, faizOranı bir değişkendir.
vade = 12                  
faizOranı = 1.47             

print(baslik)                 
print(type(baslik))           #string
print(type(vade))             #integer
print(type(faizOranı))        #float


#Örnek 2
mesaj = "Hoşgeldin"
musteriAdı = "İsmail"
musteriSoyadı= "Kılıç"
sonucMesaj = mesaj+" "+musteriAdı+" "+musteriSoyadı + "!"  #Str toplamı işlemi. DİKKAT " "
print (sonucMesaj)
print (type(sonucMesaj))


#Örnek3
numbers1 =  10 
numbers2 = 20
numbers = numbers1 + numbers2             #int toplama işlemi
  
#print(numbers1 + numbers2) #Toplama işlemi 2.yol          
