dosya=open("/Users/eylul/Desktop/Eylul/dosyatekrar.txt","r")
for i in range(5):
    a=dosya.readline()
    print(a)
dosya.close()