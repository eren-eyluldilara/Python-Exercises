dosya=open("/Users/eylul/Desktop/Eylul/dosyam.txt","r")
for i in range(7):
    oku=dosya.readline()
    print(oku)
dosya.close()