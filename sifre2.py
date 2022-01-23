giris=input("Lütfen bir şifre giriniz:")
if(len(giris)>=6 and len(giris)<=10):
    if(giris.isnumeric()==False):
        print("Girilen ifade:",giris)
    else:
        print("Şifreniz tamamen rakamdan oluşmaktadır.")
else:
    print("Karakter sayınız 6 ile 10 arasında değil")
    