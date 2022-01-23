class calisan():
    personel=[]

    def __init__(self,isim):
        self.adi=isim
        self.yetenekleri=[]
        self.personel_ekle()
    
    def personel_ekle(self):
        self.personel.append(self.adi)

    def yetenek_ekle(self,yetenek):
        self.yetenek=yetenek
        self.yetenekleri.append(yetenek)

    def yetenek_goruntule(self):
        return("{} adlı kişinin yetenekleri: {}".format(self.adi,self.yetenekleri))

kisi1=calisan("Hüseyin")
kisi1.yetenek_ekle("Dürüst")
sonuc=kisi1.yetenek_goruntule()
print(sonuc)