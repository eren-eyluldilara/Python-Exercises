#bir kelime seçilecek, kelimeyi yazdıracak, kelime uzunluğu kadar alt tire yazdıracak
#uzunluk len()
import random as rnd
liste=[["minnoş","zeytin","müezza"],["tren","otobüs","bisiklet"]]
isim=rnd.choice(liste)  
isim2=rnd.choice(isim)
print(isim2)
uzunluk=len(isim2)
print(uzunluk*" _ ")
cevap=input("Bir harf giriniz:")
s=0
for i in isim2:
    if cevap==i:
        break
    s+=1
print(s)

a=""
for i in range(len(isim2)):
    if i==s:
        a+=cevap
    else:
        a+="_"
print(a)