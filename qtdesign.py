import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class ilkPencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.basla()
    
    def basla(self):
        uic.loadUi("//Users//eylul//Desktop//Python//untitled.ui",self)
        self.pushButton.clicked.connect(self.btnTikla)
        self.show()

    def btnTikla(self):
        self.txtMetin.setText("Merhaba Dünyalı....")

app=QApplication(sys.argv)
ornek=ilkPencere()
sys.exit(app.exec_())