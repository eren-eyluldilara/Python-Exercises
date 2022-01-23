#Celcius ile Fahrenheit arasında dönüşüm yapacak python kodu
#C=(F-32)*0.555
#F=(C/0.555)+32
cevap=input("Fahrenheittan Celciusa çevirmek için 1\nCelciustan Fahrenheita çevirmek için 2 giriniz:")
if(cevap=="1"):
    deger=int(input("Lütfen bir değer giriniz:"))
    Fahrenheit=(deger/0.555)+32
    print("Fahrenheit:",Fahrenheit)
elif (cevap=="2"):
    deger=int(input("Lütfen bir değer giriniz:"))
    Celcius=(deger-32)*0.555
    print("Celcius:",Celcius)
else:
    print("Yanlış değer girdiniz")