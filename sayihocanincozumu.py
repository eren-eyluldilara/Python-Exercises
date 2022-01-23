# 1 den başlayıp kullanıcının girdiği sayıya kadar olan aralıkta rastgele bir sayı seçerek, kullanıcıdan bu sayıyı bulmasını isteyecek.
#Kullanıcının girdiği sayı,bilgisayarın tuttuğu sayıdan küçükse  yukarı, büyükse aşağı diyecek
#Kullanıcı tutulan sayıyı bilirse,bildiniz diyerek oyunu bitirecek.
import random as rnd
liste=[]
aralik=int(input("1 den itibaren tutacağım sayı için bir değer giriniz:"))
#aşka bir yol : liste=[i for i in range(1,aralik+1)]
for i in range(1,aralik+1):
    liste.append(i)
sayi=rnd.choice(liste)
print(sayi)
while(True):
    tahmin=int(input("Lütfen tuttuğum sayıyı tahmin ediniz(Çıkış için 0):"))
    if(tahmin==0):
        print("Program sona erdi")
        break
    elif(tahmin<sayi):
        print("Yukarı")
    elif(tahmin>sayi):
        print("Aşağı")
    else:
        print("Tebrikler,bildiniz.\nTuttuğum sayı:",sayi)
