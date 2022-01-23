a=0
import random as rnd
liste=[]
liste1=[["müezza","zeytin","minnoş","katmer"],["tren","otobüs","bisiklet","motosiklet"],["kitap","dergi","gazete"]]
liste_isim=rnd.choice(liste1)
isim=rnd.choice(liste_isim)
uzunluk=len(isim)

for i in range(uzunluk):
    liste+="_"

print(isim)
print(liste)

for i in range(uzunluk+3):
    giris=input("Bir harf giriniz:")
    for harf in isim:
        if(giris==harf):
            liste[a]=harf
        a+=1
    a=0
    if("_" not in liste):
        print("Tebrikler,bildiniz...",liste)
        break
    print(liste)

