dosya=open("/Users/eylul/Desktop/Eylul/dosya.txt","r")
while(True):
    oku=dosya.readline()
    if(len(oku)<2):
        break
    print(oku)