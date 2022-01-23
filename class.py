#pythonda her şey bir nesnedir
#isim="Merhaba"
#dir() bir nesnenin özelliklerini getirir

class Kedi:
    tur="Felis"
    def _init_(self,adi,yas):
        self.adi=adi
        self.yas=yas
    def Miyavla(self):
        print(self.adi,"Miyavladı")
    @classmethod
    def NefesAlma(cls):
        print("Bir",cls.tur,"daha nefes aldı")
    def _del_(self):
        print("Rest in peace")


Kedi("Melek",3)