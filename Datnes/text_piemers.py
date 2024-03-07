# Doti divi teksta faili (google drive mapē) 


# Ir teksta faili ar dažādu dzimumu vārdiem. 
#Jāuzraksta programma, kas nolasa šos failus, izveidojot vārdu sarakstus atbilstoši dzimumam (vīrieši un sievietes), 
#un pēc tam izdrukā vārdu, kurš ir visbiežāk sastopams katrā sarakstā.


# P.S. Tekstu ir iespējams sadalīt sarakstā pēc kādas konkrētas īpašības. Mēs skatījāmies, bet droši to vari pameklēt arī internetā.


#Satura nolasīšana no teksta datnes
def satura_nolasisana(fails):
    with open (fails,"r",encoding="utf-8")as f: #faila atvēršana lasīšanas režīmā
        failaSaturs = f.readlines() #Faila nolasīšana ar metodi .readlines()
        tirsSaturs = [] #Saraksta izveide priekš satura
        for vards in failaSaturs: #Cikls satura nolasīšanai
            tirsSaturs.append(vards.strip()) #.strip() noņem \n
        return tirsSaturs #Satura atgriešana


siev_fails = "Sieviešu vārdi.txt" #Sieviešu vārdu fails
vir_fails = "Vīriešu vārdi.txt" #Vīriešu vārdu fails
print(satura_nolasisana(siev_fails)) 
print(satura_nolasisana(vir_fails))

failaSatursSievietes = satura_nolasisana(siev_fails)
failaSatursViriesi = satura_nolasisana(vir_fails)

biezums = {}
for vards in failaSatursSievietes:
        
        #Salīdzina konkrēto vārdu ar izveidotās bibliotēkas/vārdnīcas saturu
        if vards in biezums:
            biezums[vards] += 1
        else:
            biezums[vards]  = 1
        
print(biezums)

#Jāizvada biežāk sastopamais vārds
print(biezums.values())
print(max(biezums, key = biezums.get))
