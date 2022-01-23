dosya=open("/Users/eylul/Desktop/Eylul/dosya.txt","r")
while(True):

    oku=dosya.readline()
    uz=len(oku)
    if uz==0:
        break
    if(uz>1):
        print(oku)
dosya.close()