"""
Json datnes teorija, apstrāde un izveidošana
"""

#Java Script Object Notation
#Teksta formāts
#Datu glabāšanai un pārvietošanai

#Datu izgūšana no vārdnīcas - atcere
# dati = {
#     "fruit": "Apple",
#     "size": "Large",
#     "color": "Red"
# }

# print(dati["fruit"])

#Atveram un nolasām failu, iegūstam tikai tekstu
fails = open("Datnes\json_piemers.json")
dati = fails.read()
print(dati[6])
fails.close()

import json as bibl

with open("Datnes\json_piemers.json","r") as fails:
    dati = bibl.load(fails)

    

