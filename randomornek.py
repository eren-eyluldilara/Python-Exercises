import random as rnd   #rnd nin karşılığı random kütüphanesi
liste=[["minnoş","zeytin","müezza"],["tren","otobüs","bisiklet"]]
isim=rnd.choice(liste)  #listelerden rastgele seçim yapmayı sağlar
isim2=rnd.choice(isim)
print(isim)
print(isim2)
print(rnd.randrange(3,9))


