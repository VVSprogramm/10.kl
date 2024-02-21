"""
Datu bāzes
MySQL

Atslēgas vārdi datu bāzēm:
Tabulas
ID - identifikators (Primary Key/Galvenā atslēga)
Lauka nosaukums
Dati
"""

import sqlite3

#savienojuma izveide
db = sqlite3.connect("izmeginajums.db")

#Tabulas izveide
db.execute("""CREATE TABLE IF NOT EXISTS edienkarte 
           (id INT PRIMARY KEY NOT NULL, 
           nosaukums TEXT NOT NULL, 
           cena REAL NOT NULL )
""")

#Datu ievietošana tabulā
# db.execute("""INSERT INTO edienkarte
#            (id,nosaukums,cena)
#            VALUES (1,'Pankūkas',2)
#            """)

# db.commit()

#Datu izvadīšana
dati = db.execute("""SELECT * FROM edienkarte""")
rezultats = dati.fetchall()
print(rezultats)