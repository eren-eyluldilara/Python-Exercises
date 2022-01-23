def yas_hesapla(yil):
    yas=int(yil)
    if(yas<=2):
        kedi_yasi=yas*7
    elif(yas>2):
        kedi_yasi=((yas-2)*4)+14
    return(kedi_yasi)
while(True):
    yas=input("Kedinizin yaşını tam sayı yıl olarak giriniz(Çıkış için 0):")
    if(yas=="0"):
        print("Program sona erdi.....")
        break
    sonuc=yas_hesapla(yas)
    print("Kediniz insan yaşı ile",sonuc,"yaşında")

