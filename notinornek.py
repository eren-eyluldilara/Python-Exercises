#in
a=["1","2",3,4,"5"]
sonuc=1 in a
print(sonuc)
sonuc1="1" in a
print(sonuc1)
#not in
sonuc2="1" not in a
print(sonuc2)

b="ozgur" #stringler liste değildir ancak liste gibi davranırlar,  tek tek harfler içinde gezinebiliriz ama sadece değerini almak için silmek ya da güncellemek için değil
sonuc3="o" in b
print(sonuc3)
print(b[0])#liste gibi indexle değere ulaştık ama bu değeri değiştiremeyiz

c=["o","z","g","u","r"]
print(c[0])
c[0]="e" #listelerde değeri değiştirebiliriz
print(c)