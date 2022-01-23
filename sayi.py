#1 den başlayıp kullanıcın girdiği sayıya kadar olan sayılardan random bir sayı belirleyecek ve bu sayıyı bulmaya çalışacağız
import random as rnd
liste=[]
sayi=int(input("Lütfen bir sayı giriniz:"))
i=1
while(sayi not in liste):
    liste.append(i)
    i+=1
    if(sayi in liste):
        break
print(liste)
secilensayi=rnd.choice(liste)
print(secilensayi)
while(True):
        tahmin=int(input("Tahmini giriniz:"))
        if(secilensayi>tahmin):
                print("Yukarı")
                
        elif(secilensayi<tahmin):
                print("Aşağı")
        elif(secilensayi==tahmin):
                print("Kazandınız")
                break
        else:
                break
    

    

