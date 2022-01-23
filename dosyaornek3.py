dosya=open("/Users/eylul/Desktop/Eylul/dosyam.txt","r")
for i in range(5):
    oku=dosya.readline()
    print(oku)
    print(len(oku))

dosya.close()

