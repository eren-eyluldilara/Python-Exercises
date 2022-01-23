#ARBITRARY ARGUMENTS-args
liste=["Özgür","Müezza","Zeytin"]
def isim(*args): #her zaman  *args bu şekilde tanımlanır
    print(args[2])
#isim("Özgür")
#isim("Özgür","Müezza","Zeytin")
isim(*liste) #mutlaka yıldız koymamız lazım bu şekilde listenin tek eleman olmadığını belirtiyoruz