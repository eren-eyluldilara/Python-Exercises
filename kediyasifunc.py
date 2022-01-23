def yas1(kedi_yasi):
        insan_yasi=kedi_yasi*7
        return(insan_yasi)

def yas2(kedi_yasi):
    insan_yasi=((kedi_yasi-2)*4)+14
    return(insan_yasi)


while(True):
    yas=int(input("Kedinizin yaşını tam sayı yıl olarak giriniz:"))
    if(yas==0):
        print("Programdan çıkıldı....")
        break
    if(yas<=2):
        kedi_yasi=yas1(yas)
        print(kedi_yasi)
    elif(yas>2):
        kedi_yasi=yas2(yas)
        print(kedi_yasi)
    else:
        print("Hata oluştu...")   
