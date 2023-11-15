"""
Dota bibliotēka, izvadi elementu - 52

 

Dots:

dati = {'Grupa': {'A': {'Jānis':[60,65,23], 'Pēteris':[68,56,25], 'Viesturs':[65,62,18]}, 'B': {'Lūkass':[58,64,20], 'Daniels':[61,52,24], 'Visvaris':[67,8,28]}}}

"""

dati = {'9.klase': {'A': {'Jānis':[60,65,23], 'Pēteris':[68,56,25], 'Viesturs':[65,62,18]}, 
                  'B': {'Lūkass':[58,64,20], 'Daniels':[61,52,24], 'Visvaris':[67,8,28]}},
        '10.kl':'vērtība'}

print("52")
print('Daniels'[1])
print('9.klase','B','Daniels'[1])
print(dati['9.klase']['B']['Daniels'][1])



""""
Draugiem jāaprēķina, cik izmaksās apdrukātu T-kreklu pasūtīšana, ņemot vērā, ka cena ir
atkarīga no apdrukas veida un kreklu skaita.

#Specifikācija

● Funkcijai pasuti_tkreklus ir divi parametri saskaņā ar formātu pasuti_tkreklus(skaits, apdruka). 
Parametrs skaits ir vesels skaitlis (pasūtamo kreklu skaits), parametrs apdruka ir simbolu virkne. #teksta mainīgais
● Parametrs apdruka var būt simbolu virkne, kam atļautas trīs vērtības: TEKSTS, ZIME vai FOTO. 
Cena attiecīgi ir 5 EUR, 7 EUR un 20 EUR.
● Pasūtījumiem, kas pārsniedz 100 EUR, tiek piemērota 5% atlaide no pasūtījuma summas.

"""
def pasuti_tkreklus(skaits, apdruka):
    #apdruka =  TEKSTS, ZIME vai FOTO
    #cenas = 5 EUR, 7 EUR un 20 EUR
    kopeja_cena = 0
    if apdruka == "TEKSTS":
        kopeja_cena = 5 * skaits
    elif apdruka == "ZIME":
        kopeja_cena = 7 * skaits
    elif apdruka == "FOTO":
        kopeja_cena = 20 * skaits
    
    #kopeja_cena > 100 - 5% atlaide
    #kopeja_cena < 100 - nav atlaides
    if kopeja_cena > 100:
        # atlaide = kopeja_cena * 0.05
        # kopeja_cena = kopeja_cena - atlaide
        
        #Ja atlaide ir 5%, tad palikusī summa būs 95% - 0.95
        kopeja_cena = kopeja_cena * 0.95
    
    print(kopeja_cena)
    
pasuti_tkreklus(5,"TEKSTS")
pasuti_tkreklus(10,"ZIME")
pasuti_tkreklus(5,"FOTO")
pasuti_tkreklus(6,"FOTO")
pasuti_tkreklus(4,"foto")

# def pasuti_tkreklus(tekst,zime,foto):

#   kopeja_cena = tekst*zime*foto

#   print("Apdruka vienam kreklam",kopeja_cena)

# pasuti_tkreklus(5,7,20)

#Par procentu piemērošanu mēs nebījām ņēmuši kā to var izpildīt
