"""
Apgalvojumi jeb if, else, elif statements
"""

#Sintakse:
"""
if nosacijums:
    print("Darbība")
else:
    print("Notiek tad, ja neizpildās nosacījums")
"""

gadi = 50 #Mainīgā gadi definēšana un vērtības piešķiršana (inicializācija)

if gadi<18:
    print("Nepilngadīga persona")
else:
    print("Pilngadīga persona")


#Nedēļas dienu piemērs

nedelasDiena = 4
noskanojums = "ghkhk"
if nedelasDiena==1:
    print("Pirmdiena")
if nedelasDiena==2:
    print("Otrdiena")
elif nedelasDiena==3:  #Nākošo iespējamo pārbaudi
    print("Trešdiena")
elif nedelasDiena==4:
    print("Ceturtdiena")
    if noskanojums=="Labi":
        print("Cik jauki")
    else:
        print("Turies!")
elif nedelasDiena==5:
    print("Piektdiena")
elif nedelasDiena==6:
    print("Sestdiena")
elif nedelasDiena==7:
    print("Svētdiena")


print("Apgalvojums ir beidzies")