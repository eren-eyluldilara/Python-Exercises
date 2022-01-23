#burada while conditiona göre 0 değeri verilidiğinde direk programdan çıkıyor.
while(True):
    yas=int(input("Kedinizin yaşını tam sayı yıl olarak giriniz:"))
    if(yas==0):
        print("Programdan çıkıldı....")
        break
    if(yas<=2):
        kedi_yasi=yas*7
        print(kedi_yasi)
    elif(yas>2):
        kedi_yasi=((yas-2)*4)+14
        print(kedi_yasi)
    else:
        print("Hata oluştu...")