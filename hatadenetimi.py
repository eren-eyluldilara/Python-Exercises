try:
    a=int(input("Bir sayı giriniz:"))
    sonuc=a-5
    print(sonuc)
except Exception as hata:
    print("Bir hata oluştu",hata)
finally:
    print("Bu kısım her şartta çalışır")