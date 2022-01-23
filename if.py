yas=int(input("Yaşınızı giriniz:"))
if(yas<18):
    print("Reşit değilsiniz.")
elif((yas>=18)and(yas<25)):
    print("Hayat size çok güzel")
#else de yeni bir şart koşmuyoruz ama elifte şart koşuluyor
else:
     print("Reşitsiniz.")  
