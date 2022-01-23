yas=int(input("Lütfen yaşınızı giriniz:"))
if(yas<18):
    print("Tek doz aşı olabilirsiniz.")
elif((yas>=18)and(yas<=5)):
    print("Çift doz aşı olabilirsiniz")
elif((yas>=25)and(yas<50)):
    print("Üç doz aşı olabilirsiniz.")
elif((yas>=50)and(yas<70)):
    print("Dört doz aşı olabilirsiniz")
else:
    print("Beş doz aşı olabilirsiniz")

