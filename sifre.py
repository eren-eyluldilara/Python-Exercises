#Kullanıcılardan bir veri girmesini isteyiniz.
#Giriş en az 6 en fazla 10 karakter olabilir.Ayrıca hem harf hem de sayı içermellidir.
#Şartlar sağlanmıyorsa, sağlanmadığını kullanıcıya bildiriniz.
sifre=input("Lütfen şifreyi giriniz:")
sifreuzunlugu=len(sifre)
if((sifreuzunlugu>=6)and(sifreuzunlugu<=10)):
    if((sifre.isalpha()==0)and(sifre.isnumeric()==0)):
      print("Şifrenizi girdiniz.")
    else:
        print("Şifreniz sadece harf veya sadece rakam içeriyor.")

else:
    print("Şifreniz 6-10 karakter uzunluğunda değil.")
