"""
Uzraksti funkciju izmaksas, kas aprēķina ābolu ievārījuma izmaksas, ja dota cukura cena kg.
Un cukura, ābolu un garšvielu daudzums ievārījuma receptē.

Dots:
recepte = {"cukurs":0.6, "kanelis":0.008, "aboli":1.0, "udens":0.2}
cenas = {"cukurs":0.75, "kanelis":30.0, "aboli":0.0, "udens":0.0}

Sagaidāmais rezultāts:
izmaksas(recepte,cenas) ------->  15 EUR
"""
recepte1 = {"cukurs":0.6, "kanelis":0.008, "aboli":1.0, "udens":0.2}
cenas1 = {"cukurs":0.75, "kanelis":30.0, "aboli":0.0, "udens":0.0}


def izmaksas_receptei(recepte,cenas):  #Iekavās atrodas argumenti
    #Funkcija aprēķina izmaksas dotajai receptei
    #Summējot visas sastāvdaļu cenas

    receptesCena = 0
    # cukuraCena = recepte["cukurs"] * cenas["cukurs"]
    # kanelaCena = recepte["kanelis"] * cenas["kanelis"]
    # aboliCena = recepte["aboli"] * cenas["aboli"]
    # udensCena = recepte["udens"] * cenas["udens"]
    # receptesCena = cukuraCena+kanelaCena+aboliCena+udensCena

    #Uzlabot koda efektivitāti, izmantojot ciklu
    for sastavdala in recepte:
        daudzums = recepte[sastavdala]
        #receptesCena = receptesCena + (daudzums * cenas[sastavdala])
        receptesCena += daudzums * cenas[sastavdala]
        print("Apļa beigas")

    print("Kopējā cena:",receptesCena)  
    return receptesCena #return atslēgas vārds, dod iespēju iegūt vērtību no funkcijas

izmaksas_receptei(recepte1,cenas1)    #Izsaucot funkciju, iekavās tiek likti mainīgie, kuri ir definēti programmā


def izmaksas_kopa():
    #funkcija aprēķina ievārījuma sastāvdaļu izmakasas, atkarībā no dotā ābolu daudzuma

    