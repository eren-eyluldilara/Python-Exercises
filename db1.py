import sqlite3 as sql
db=sql.connect("//Users//eylul//Desktop//Eylul//KUTUPHANE.db")
imlec=db.cursor()
imlec.execute("DELETE * FROM ogrenci;")
veri=imlec.fetchall()
imlec.close()
db.close()