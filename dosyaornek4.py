dosya=open("/Users/eylul/Desktop/Eylul/dosyam.txt","r")
while(True):
    oku=dosya.readline()
    if(len(oku)<2):
        print("Dosya sonuna gelindi")
        break
    print(oku)
dosya.close()