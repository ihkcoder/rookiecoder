"""
1-Kullanıcadan 2 vize (½60) ve final (½40) notunu alıp ortalama hesaplayınız
  Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
       
       a-) Ortalama 50 olsa bilde final notu en az 50 olmalıdır
       
       b-) Finalden 70 alındığında ortalamanın öenmi olmasın.
"""

vize1 = float(input("1. Vize sonucu: "))

vize2 = float(input("2. Vize sonucu: "))

final = float(input("Final sonucu: "))

ortalama = ((vize1 + vize2)/2)*0.6 + (final * 0.4) 

if (ortalama >=50) and (final >= 50) or (final >= 70):
     print(f"{ortalama} not ortamasıyla dersten geçtiniz ")

elif (ortalama < 50):
     print(f"{ortalama} not ortalamasıyla derstden kaldınız ")

elif (final < 50):
     print(f"final notunuz 50'den düşük olduğu için kaldınız")


"""
2-  Kişinin ad, kilo, ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
     
     Formül: (Kilo / boy uzunluğunun karesi) 
     
     Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
     0-18.4      => Zayıf
     18.5-24.9   => Normal
     25.0-29.9   => Fazla Kilolu
     30.0-34.9   => Şişman (Obez)
"""

name = (input("Adını gir : "))

length = float(input("Boyunu gir : "))  # Lütfen nokta koymayı unutmayın Örnek:(1.80)

weight = float(input("Kilonu gir : "))

index = weight/(length ** 2) 

if (index > 0) and (index <= 18.4):
     print(f"{name} kilo indeksin {index} ve kilosu değerlendirmeniz zayıf")

elif(index > 18.5) and (index <= 24.9):
     print(f"{name} kilo indeksin {index} ve kilosu değerlendirmeniz normal")

elif(index > 25.0) and (index <= 29.9):
     print(f"{name} kilo indeksin {index} ve kilosu değerlendirmeniz kilolu")

elif(index > 30.0) and (index <= 34.9):
     print(f"{name} kilo indeksin {index} ve kilosu değerlendirmeniz obez")

else:
     print(f"{name} kilo indeksin {index} ve kilosu değerlendirmeniz obez")
