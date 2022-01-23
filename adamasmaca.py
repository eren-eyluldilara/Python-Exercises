import random as rnd
animalNames = ["dog", "cat", "bird", "snake"]
personNames = ["mehmet", "ahmet", "özgür","ali"]
carNames = ["mitsubishi", "renault","bmw", "auidi"]
finalList = [animalNames, personNames, carNames]
rndList = rnd.choice(finalList) #finallistten random bir liste seçiyor
kelime = rnd.choice(rndList) #listeden random bir index seçiyor
print(kelime) #seçilen kelimeyi bastırdık
canHakki = int((len(kelime)/2)*3) #can hakkı seçilen kelimenin yarısının üç katı kadar
print("can: ",  canHakki) #canhakkını bastırıyor
indexLer = [] #yeni liste yarattık
while (canHakki != 0): #canhakkı sıfır olmadığı sürece while loop çalışacak
    a = [] #yeni liste
    s = 0 #sayaça sıfır verdik
    girilenHarf = input("harf: ") #tahmin edilen harfi aldık
    for h in kelime: #seçilen kelimedeki tüm harfler h değerinde
        if (girilenHarf in h) and (not s in indexLer): #tahmin ettiğimiz harf h da  varsa ve sayaç indexler listesinde değilse
            indexLer.append(s) #indexler listesinde sayacı ekle
        s +=1 #sayacı bir arttır
    for i in range(len(kelime)): #seçilen kelimenin harf sayısını buluyor
        if i in indexLer: # eğer o harf sayısı indexlerde varsa
            a.append(kelime[i]) #a listesine kelimenin harfini ekliyoruz
        else:
            a.append("_") #değilse boşluk ekliyoruz
    tahmin = ""
    for i in a: #seçilen kelimedeki harflerden birisi tahmin edilen harf ise
        tahmin += i #tahmine ekledik o harfi
        print(tahmin) #tahmini ekrana bastır
    if tahmin == kelime: #eğer tahmin ile seçilen kelime aynıysa
        print("kazandınız") #kazandın
        break
    canHakki -=1 #her loopta can hakkından bir azalıyor
    print("kalan can: ", canHakki) #kalan can hakkını gösteriyor
if canHakki == 0: #canhakkı sıfır olduğunda
    print("kaybettiniz") #kaybettin