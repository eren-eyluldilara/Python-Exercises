class bir():
    def __init__(self):
         self.a="Selam Dünyalı...."
    
    def met1(self):
        print("Merhaba Uzaylı")
   
    def met2(self):
        print(self.a)

class iki(bir):
    def __init__(self):
        super().__init__()
        self.b="Selam Marslı"
    def met3(self):
        print(self.b)

ornek=iki()
ornek.met1()
ornek.met3()
ornek.met2()