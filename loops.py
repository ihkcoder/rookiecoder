"""
* Bir dizi üzerinde yineleme yapmak için  "for" döngüsü kullanılır

** "for" döngülerini bir eleman grubundaki (list, tuple, dictionary, set ya da string) 
her bir elemana ulaşmak için kullanırız.

*** Python'da list verileri üzerinde for döngüsü ile her bir elemana ulaşabiliriz.

**** Pythondaki "in" operatörü bir elemanın başka bir listede, demette () veya stringte 
(karakter dizileri) bulunup bulunmadığını kontrol eder. 

"""
# For Loops

sayilar = [1,2,3,4,5]
for sayi in sayilar:
   
     print(sayi)


isimler = ['ismail','elif','fatma']
for isim in isimler:
    
     print(f'my name is {isim}')


meyveler = ["apple", "banana", "cherry"]
for meyve in meyveler:
     
     print(meyve)
