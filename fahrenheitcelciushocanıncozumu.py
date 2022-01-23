menu="""
1. Celcius-Fahrenheit
2. Fahrenheit- Celcius
3. Çıkış
"""
while(True):
    print(menu)
    secim=input("Seçiminizi Giriniz:")
    if(secim=="1"):
        C=int(input("Celcius değerini giriniz:"))
        F=(C/0.555)+32
        print("Fahrenheit değeri:",F)
    elif(secim=="2"):
        F=int(input("Fahrenheit değerini giriniz:"))
        C=(F-32)*0.555
        print("Celcius Değeri:",C)
    elif(secim=="3"):
        print("Program sona erdi")
        break
    else:
        print("Yanlış değer girdiniz,tekrar deneyiniz...")
