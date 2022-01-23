#kedinin yaşı tam sayı girilmeli
#ilk 2 yıl için bir yaş 7 insan yılına denk geliyor
#ondan sonraki her yas 4 insan yılına denk geliyor
kediyasi=int(input("Lütfen kedinizin yaşını giriniz:"))
if(kediyasi<=2):
    insanyasi=kediyasi*7
    print("Kediniz ",insanyasi,"yaşında")
elif(kediyasi>2):
    yeniyas=kediyasi-2
    insanyasi=(yeniyas*4)+14
    print("Kediniz ",insanyasi,"yaşında")