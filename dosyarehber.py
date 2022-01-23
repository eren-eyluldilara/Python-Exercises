

def veri_al():
    liste1=[]
    liste=["ADI: ","SOYADI: ","TELEFON: "]
    for i in liste:
        isim=input(i)
        liste1.append(isim)
    return liste1

def kaydet(liste):
    dosya=open("/Users/eylul/Desktop/Eylul/dosya.txt","a")
    for i in range(len(liste)):
        dosya.write(liste[i]+"\n")
    return("Dosyalar kaydedildi...")
a=kaydet(veri_al())
print(a)