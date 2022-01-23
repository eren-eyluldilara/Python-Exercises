adres="//Users//eylul//Desktop//Eylul//dosya.txt"
menu="""
1-Yeni Kayıt
2-Arama
3-Liste
4-Çıkış
"""

def isim_sor():
    kayit_liste=[]
    liste1=["ADI:","SOYADI:","TELEEFON:"]
    for i in liste1:
        isim=input(i)
        kayit_liste.append(isim)
    return kayit_liste

def kaydet(liste):
    dosya=open(adres,"a")
    for i in  range(len(liste)):
        if i==2:
            dosya.write(liste[i]+"\n")
        else:
            dosya.write(liste[i]+",")
    dosya.close()
    return("Veriler kaydedildi...")




