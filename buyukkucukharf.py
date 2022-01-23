#klavyeden girilen bir string ifadenin içerisinde kaç tane büyük ve kaç tane küçük harf olduğunu bulan fonksiyonu yazınız.
#Hizli Kahverengi Tilki
#c.isupper(),c.islower()
#buyukharf.append(1)
def harf(kelime):
    liste=[]
    kucuk_harf=0
    buyuk_harf=0
    for i in kelime:
        if(i.isupper()):
            buyuk_harf+=1
        elif(i.islower()):
            kucuk_harf+=1
    liste.append(kucuk_harf)
    liste.append(buyuk_harf)
    return liste
a=harf("Hizli Kahverengi Tilki")
print(a)