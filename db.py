import sqlite3 as sql
kodlar=["DELETE FROM ogrenci WHERE ogrenci.OgrenciId=16;","DELETE FROM odunc WHERE odunc.OgrenciId NOT IN(SELECT ogrenci.OgrenciId FROM ogrenci);"]

db=sql.connect("//Users//eylul//Desktop//Eylul//KUTUPHANE.db")
imlec=db.cursor()

imlec.execute(kodlar[0])
db.commit()

imlec.execute(kodlar[1])
db.commit()

imlec.close()
db.close()
print("İşlem başarılı")