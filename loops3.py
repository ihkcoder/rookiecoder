"""
* "range" kelimesi İngilizcede ‘aralık’ anlamına gelir.

** Python’da range() fonksiyonunu belli bir aralıkta bulunan sayıları göstermek için kullanıeız.

***Üç tane parametre alır. İki parametreli şeklinde de kullanılabilir.
Birinci parametre başlangıç aralığı, ikinci parametre bitiş aralığı,
üçüncü parametre ise artış miktarıdır.

**** range() fonksiyonunun 1. parametre  formülü şöyledir:
range(sayi)

***** range() fonksiyonunun 2. parametre  formülü şöyledir:
range(ilk_sayı, son_sayı)

******  range() fonksiyonunun 3. parametre formülümü şöyledir:
range(ilk_sayı, son_sayı, atlama_değeri)

******* print() fonksiyonunun sep parametresi yardımıyla 
bu çıktıyı istediğiniz gibi düzenleyebiliriz.

"""

#-------------------------Range-------------------------#

for i in range(10):
     print(i)


for i in range(3,20):
     print(i)


for i in range(10,50,5):
     print(i)


for x in range(6):
  if x == 3: break
  print(x)

else:
  print("Finally finished!")


print(*range(10))               # Sayılar yan yana çıkar.

print(*range(10), sep=", ")     # Sayıların aralarına virgül koyduk.

