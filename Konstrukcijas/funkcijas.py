"""
02.11.
Funkcijas
"""

#Sintakse
"""
Atslēgas vārds:
def

def funkcijas_nosaukums():
    funkcijas kods

Izsaukšana:
funkcijas_nosaukums()
"""

def pirma_funkcija():  #() - iekavās ir iespējams pievienot argumentus jeb saņemtās vērtības
    print("Mana pirmā funkcija, Juhuuuuu!!!!")

#Katru funkciju nepieciešams atsevišķi palaist
pirma_funkcija()
pirma_funkcija()
pirma_funkcija()
pirma_funkcija()
pirma_funkcija()

atbilde = input("Gribi, es ar kaut ko palielīšos?")

if atbilde == "Jā":
    pirma_funkcija()
else:
    print("Nu labi ;(")

def otra_funkcija():
    pirma_funkcija()
    print("funkcija funkcijā!")

otra_funkcija()