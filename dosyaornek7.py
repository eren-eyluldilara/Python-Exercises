dosya=open("/Users/eylul/Desktop/Eylul/dosya.txt","r")
for i in range(4):
    oku=dosya.readline()
    print(oku)
dosya.close()