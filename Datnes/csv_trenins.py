import csv 

#Funkcija datnes nolasīšanai
def csv_lasisana(fails):
    
    with open(fails,'r', encoding="UTF-8") as fails:
        lasit_csv = csv.reader(fails)
        saturs1 = []
        for rinda in lasit_csv:
            saturs1.append(rinda)
        return saturs1

# #Funkcija datu salīdzināšanai
def salidzini_datus(datiViens,datiDivi):

    # datiViens.csv = salidzini_datus(datiViens)
    # datiDivi.csv = salidzini_datus(datiDivi)

    vienadie = []
    #Pirmā faila rindu nolasīšana
    for rinda in datiViens:
        
        #Salīdzina konkrēto rindu ar otrā faila saturu
        if rinda in datiDivi:
            vienadie.append(rinda)

    if len(vienadie) > 0:
        print("Sakrīt!")
    # datiViens.csv = set(datiViens.csv.split())
    # datiDivi.csv = set(datiDivi.csv.split())

#Failu nosaukumi
datneDivi = "datiDivi (1).csv"
datneViens = "datiViens.csv"

datiViens = csv_lasisana(datneViens)
print(datiViens)
datiDivi  = csv_lasisana(datneDivi)
print(datiDivi)
 

salidzini_datus(datiViens, datiDivi)


#Dotas divas csv datnes (skat.google drive).

# Izveido funkciju, kas nolasa datus no vienas datnes.
# Izveido funkciju datu salīdzināšanai, kurā pārbaudi, vai ir dati, kas ir unikāli, ja šādi dati ir, izvadi - Ir unikāli!

#Funkcija datnes nolasīšanai
def csv_lasisana(fails):
    
    with open(fails,'r', encoding="UTF-8") as fails:
        lasit_csv = csv.reader(fails)
        saturs1 = []
        for rinda in lasit_csv:
            saturs1.append(rinda)
        return saturs1

# #Funkcija datu salīdzināšanai
def salidzini_datus_unikalie(datiViens,datiDivi):

    # datiViens.csv = salidzini_datus(datiViens)
    # datiDivi.csv = salidzini_datus(datiDivi)

    unikalie = []
    #Pirmā faila rindu nolasīšana
    for rinda in datiViens:
        
        #Salīdzina konkrēto rindu ar otrā faila saturu
        if rinda not in datiDivi:
            unikalie.append(rinda)

    #Otrā faila rindu nolasīšana
    for rinda in datiDivi:
        
        #Salīdzina konkrēto rindu ar otrā faila saturu
        if rinda not in datiViens:
            unikalie.append(rinda)

    if len(unikalie) > 0:
        print("Ir unikāli!")
    # datiViens.csv = set(datiViens.csv.split())
    # datiDivi.csv = set(datiDivi.csv.split())

#Failu nosaukumi
datneDivi = "datiDivi (1).csv"
datneViens = "datiViens.csv"

datiViens = csv_lasisana(datneViens)
print(datiViens)
datiDivi  = csv_lasisana(datneDivi)
print(datiDivi)
 

salidzini_datus_unikalie(datiViens, datiDivi)
