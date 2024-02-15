"""
CSV datnes lasīšana, rediģēšana un izveidošana
"""
htmlkodam = "<!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>"
with open("htmlMeginjaums.html","r", encoding="UTF-8") as fails:
    print(fails.read())


# Fails tiek atvērts kā teksta fails
fails = open("csv_piemers.csv", encoding="UTF-8")
print(fails.read())
fails.close()

#Lai nolasītu csv datni, nepieciešama bibliotēka

import csv

fails = open("csv_piemers.csv", encoding="UTF-8")

lasit_csv = csv.reader(fails) #Mēs nolasām failu #Objekta izveide
print(lasit_csv) #Redzam tikai objektu

#Kolonnu nosaukumi

kolonnuNosaukumi = next(lasit_csv)
print(kolonnuNosaukumi)

#Satura nolasīšana
#Cikls
saturs = []
for rinda in lasit_csv:
    saturs.append(rinda)

print(saturs)

fails.close()

for rinda in saturs:
    print(rinda)
    print(rinda[0])
    # for dati in rinda:
    #     print(dati)

#Jauna faila izveide

kolonnuNosaukumi = ['Vārds','Vecums','Mācību iestāde']

vards = input("Uzraksti savu vārdu: ")
vecums = input("Uzraksti savu vecumu: ")
macibuIestade = input("Uzraksti savas mācību iestādes nosaukumu: ")

saturs = [vards,vecums,macibuIestade]

with open("csv_jaunsFails.csv","a", encoding="UTF-8") as fails:
    csvwrite = csv.writer(fails) #Objekta izveide
    csvwrite.writerow(kolonnuNosaukumi)
    csvwrite.writerow(saturs)
