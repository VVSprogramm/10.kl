"""
for cikla treniņa uzdevums - taisnleņķa trijstūra izvade
"""

#Uzdevums:
#Izveido programmu, kas izvada apgrieztu tainsleņķa trijstūri
#*****
#****
#***
#**
#*

rindas = 5

#nested loops jeb cikli, kuri atrodas viens otrā

#ārējais cikls
for rinda in range(0,rindas): #range() - nosaka no kura līdz kuram skaitlim atkārtosies cikls
    #print("Šī ir rinda: ", rinda)
    print()

    #iekšējais cikls
    for simboluSkaits in range(rindas-rinda):
        #print("*") #print() funkcijai pēc noklusējuma beigās ir vērtība, kas pārceļ jaunā rindā
        print("*",end=" ")
    