#bu kodda while condition yüzünden 0 diyip çıkmak istediğimizde kedi yaşı 0 diyip çıkıyor!

yas=1
while(yas!=0):
    yas=int(input("Kedinizin yaşını tam sayı yıl olarak giriniz(Çıkış için O):"))
    if(yas<=2):
        kedi_yasi=yas*7
        print(kedi_yasi)
        
    elif(yas>2):
        kedi_yasi=((yas-2)*4)+14
        print(kedi_yasi)
        
    else:
        print("Hata oluştu...")
