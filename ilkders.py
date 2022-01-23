sevda=1# sevdanın tipi şu an integer
sevda="1"#sevdanın tipi şu an string
leyla="2"
print(sevda+leyla)#12 olacak çünkü 1 ve 2 string stringlerin toplamı 12 ediyor
#print((sevda+leyla)+3)hata vermesi gerekiyor çünkü bir string ilr integerı toplamaya çalışıyoruz
sevda=1
leyla=2
print((leyla+sevda)+3)#çıktı 6 olmalı,çünkü sevda ve leyla şu anda integer 
#BODMAS-Brackets Off- Division,Multiplication,Addition,Substraction
#Değişkenler:
#1.)Sayısal tip değişkenler (integer-int)
#2.)Metin tipi değişkenler (atring ifadeler-her zaman çift tırnak içine alınır)
#3.)Liste tipi değişkenler
#Değişken Tanımlama:
#1.)Türkçe karakterler içeremezler
#2.)alt tire hariç özel karakterler içeremezler
#3.)Rakamla başlayamazlar
giris=input("Birşeyler giriniz:")#input fonskiyonu ile aldığımız herşey string olarak gelir,eğer değeri başka tipler olarak almak istersek input fonksiyonuna int,double,float etc eklemeliyiz.
print(giris)
print("Merhaba girdiğiniz veri:",giris)#giris değeri string
print("Merhaba girdiğiniz veri:"+giris)#herzaman kullanılacak birşey değil, virgül kullanmak daha doğru
giris=int(input("Birşeyler giriniz:"))#ya da int(giris) diyebiliriz
sonuc=str(giris+3)
#print("Merhaba girdiğiniz veri:"+giris+3)#buradaki iki + operatörünün de işi farklı ,ilk artı concatenate işlemi için ve concatenate işlemi sadece stringler için
print("Merhaba girdiğiniz veri:",int(giris)+3)
print("Merhaba girdiğiniz veri:",giris+3)
print("Merhaba girdiğiniz veri:"+str(giris+3))
print("Merhaba girdiğiniz veri:"+sonuc)