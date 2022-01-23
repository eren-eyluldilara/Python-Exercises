class Deneme():
    def __init__(self,data):
        self.a=data
        print("Bu başlangıçta çalışır")
        print(self.a)
    def dene(self):
        b=67
        return b
    def _del_(self):
        print("Bu bitişte çalışır")

a=Deneme(46)
b=a.dene()
print(b)