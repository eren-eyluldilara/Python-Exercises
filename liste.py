veri="vektorel"
print(veri[-1])#indexi [] bu parantezle alıyoruz ve -1 dediğimizde sondan başlıyor
print(veri[2])
print(veri[:])
print(veri[2:4])#2 ve 3 indexinin değerini verecek
#liste string ,integer, karışık veri tipinde de olabilir
liste1=[1,2,3,4,5,6]
print(liste1[0])
liste2=[1,["Minnoş","Zeytin","Müezza"],"Merhaba",3,4,5,6]
print(liste2[2])
print(liste2[1])
print(liste2[1][1])#zeytin
liste=[]#liste tanımlama
liste+="Müezza"#listeye eleman ekleme, her harfi ayrı ayrı alıp ekledi
print(liste)
liste+=["Müezza"]#listeye eleman ekleme,müezzayı tek bir karakter olarak ekledi
print(liste)
a=5
a=a+1
a+=1
print(a)
a=5
b=10
print(b/a)#tek slash koyunca float bölmesi yapıyor
print(int(b/a))
print(b//a)#çift slash koyunca int bölmesi yapıyor
