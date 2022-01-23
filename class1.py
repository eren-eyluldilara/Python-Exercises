#isim="Merhaba"
#print(dir(isim))

class Kedi:
    selam="Merhaba" #class attribute

print(Kedi.selam)

class Kedi:
    selam="Merhaba"#class attribute
    print(selam) #class method

Kedi()

class Ornek():
    isim="Hüseyin" #class method çağırmak için nesneye gerek yok
    def yaz(self): #instant method , nesne ile çalışır
        self.isim="Hüseyin"
        print("Merhaba",self.isim)


Ornek1=Ornek()
Ornek1.yaz()

nesne1=Ornek()
nesne1.yaz()


class Calisan():
    yetenekler=[]
    unvani="isci"
    maasi="1500"

Calisan.yetenekler.append("çalışkan")
Calisan.yetenekler
isci1=Calisan()
isci1.yetenekler.append("Dürüst")
isci2=Calisan()
isci2.yetenekler.append("Sadık")
print(isci2.yetenekler)

