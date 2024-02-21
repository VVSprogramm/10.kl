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
print(type(dati))
print(dati[6])
fails.close()

import json as bibl

with open("Datnes\json_piemers.json","r") as fails:
    dati = bibl.load(fails)
    print(dati)
    print(type(dati))

print(dati["fruit"])

dati2 = {
    "atslega":"dati"
}
parveidoti_dati = bibl.dumps(dati2,indent=2)
print(parveidoti_dati)
print(type(parveidoti_dati))

with open("Datnes\json_meginajums.json","w") as fails:
    
    bibl.dump(parveidoti_dati,fails,indent=2)
    

    

