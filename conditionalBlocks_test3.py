# 1- Email ve parola bilgileri ile giriş kontrolü yapınız.

email = "klc63"
password = "cimbom1905"

girilenEmail = input("Email: ")
girilenPassword = input("Parola: ")

if (girilenEmail == email): 
     if (girilenPassword == password ):
          print("Giriş Başarılı") 
     else:
          print("Emailiniz hatalı")

else:
     print("Parola hatalı")

print("İşlem sonu")

# 2- Girilen üç sayının büyüklük olarak karşılaştırınız

sayi1  = int(input("1.Sayıyı gir : "))
sayi2  = int(input("2.Sayıyı gir : "))
sayi3  = int(input("3.Sayıyı gir : "))

if (sayi1 > sayi2) and (sayi1 > sayi3): 
     print (f"{sayi1} sayisı en büyük sayıdır") 

elif (sayi2 > sayi1) and (sayi2 > sayi3):
     print (f"{sayi2} sayisı en büyük sayıdır")  

else:
     print (f"{sayi3} sayisı en büyük sayıdır") 
