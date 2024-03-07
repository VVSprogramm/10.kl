# Doti divi teksta faili (google drive mapē) 


# Ir teksta faili ar dažādu dzimumu vārdiem. 
#Jāuzraksta programma, kas nolasa šos failus, izveidojot vārdu sarakstus atbilstoši dzimumam (vīrieši un sievietes), 
#un pēc tam izdrukā vārdu, kurš ir visbiežāk sastopams katrā sarakstā.


# P.S. Tekstu ir iespējams sadalīt sarakstā pēc kādas konkrētas īpašības. Mēs skatījāmies, bet droši to vari pameklēt arī internetā.


# viriesuvardi = [ ]
# sieviesuvardi = [ ]


# def csv_lasisana(sieviesuvardi,viriesuvardi):

#  with open(sieviesuvardi,viriesuvardi, 'r',encoding="UTF-8") as fails:
#        for rinda in fails:
#         vārds = rinda.strip()
#         dzimums = input("Lūdzu, ievadiet dzimumu (v vai s) vārdam '{}': ".format(vārds))
#         if dzimums == 'v':
#             viriesuvardi.append(vārds)
#         elif dzimums == 's':
#             sieviesuvardi.append(vārds)


# visbiežākaisvīriešuvārds = max(set(viriesuvardi), key = viriesuvardi.count)
# visbiežākaissieviešuvārds = max(set(sieviesuvardi), key = sieviesuvardi.count)


# print("Visbiežāk sastopamais vīriešu vārds ir: {}".format(visbiežākaisvīriešuvārds))
# print("Visbiežāk sastopamais sieviešu vārds ir: {}".format(visbiežākaissieviešuvārds))

# data = {}
# data["Anna"]  = 1
# print(data)

with open ("Sieviešu vārdi.txt","r",encoding="utf-8")as f:
    failaSatursSievietes = f.readlines()

with open ("Vīriešu vārdi.txt","r",encoding="utf-8")as f:
    failaSatursViriesi = f.readlines()

print(failaSatursSievietes)
print(failaSatursViriesi)
biezums = {}
for vards in failaSatursSievietes:
        
        #Salīdzina konkrēto vārdu ar tā paša faila saturu
        if vards in biezums:
            biezums[vards] += 1

        else:
            biezums[vards]  = 1

        
print(biezums)

#Jāizvada biežāk sastopamais vārds
print(biezums.values())
print(max(biezums, key = biezums.get))
