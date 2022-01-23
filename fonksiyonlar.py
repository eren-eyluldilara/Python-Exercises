#FONKSIYONLAR
# def function_name (parameters):
    #body

from typing import Type


def fonk():  #fonksiyon tanımı
    print("Merhaba Python")

fonk()  #fonksiyonu çağırma, function call 


def a(isim):
    print(isim)

a(12)

def fonksiyon(a):
    print(a)

fonksiyon(1)
print(type(fonksiyon))


def topla(sayi1,sayi2):
    print(sayi1+sayi2)
topla(2,4)
#topla(2) iki parametresi var ama bir gönderdiğimiz için hata verecek
#topla() iki parametresi var ama  hiç parametre göndermedik , hata verecek

def topla1(sayi1=3,sayi2=5):
    print(sayi1+sayi2)
topla1()
topla1(6)
topla1(6,3)
topla1(sayi2=6,sayi1=3)

