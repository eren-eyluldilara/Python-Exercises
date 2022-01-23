#a+b>c,a-b<c doğruların üçgen oluşturup oluşturmadığını kontrol etme
dogru1=int(input("İlk uzunluğu giriniz:"))
dogru2=int(input("İkinci uzunluğu giriniz:"))
dogru3=int(input("Üçüncü uzunluğu giriniz:"))
islem1=dogru1+dogru2
islem2=abs(dogru1-dogru2)#abs() mutlak değeri alan fonksiyon
if((islem1>dogru3)and(islem2<dogru3)):
    print("Bu üç doğru üçgen oluşturabilir.")
else:
    print("Bu üç doğru üçgen oluşturamaz.")
    