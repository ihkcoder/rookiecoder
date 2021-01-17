"""
* "break" kelimesi İngilizce’de ‘kırmak, koparmak, bozmak’ gibi anlamlara gelir.

** "break" deyimiyle, tüm öğeler arasında döngü oluşturmadan önce döngüyü durdurabiliriz:

*** "continue" ifadesiyle, döngüdeki mevcut yinelemeyi durdurabilir ve
bir sonraki ile devam edebiliriz

**** continue deyiminin görevi kendisinden sonra gelen her şeyin
es geçilip döngünün başına dönülmesini sağlamaktır.

"""

#-------------------------Break-------------------------#

fruits = ["apple", "banana", "cherry", "strawberry"]

for x in fruits:
     if x == "cherry":
          break
     
     print(x)

for i in range(11):
     
     if i > 5:
          break
     
     print(i)

#-------------------------Continue-------------------------#

fruits = ["strawberry", "apple", "banana", "cherry"]

for x in fruits:
     if x == "apple":
          continue
     
     print(x)


for i in range(11):
     
     if i == 7:
          continue
     
     print(i)
