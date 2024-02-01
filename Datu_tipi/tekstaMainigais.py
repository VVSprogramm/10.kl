'''
Datu tips - String (teksts,virkne)
str
14.09.2023
'''

x=5 #bez pēdiņām - vesels skaitlis
y='5' #ar pēdiņām - tekstu

print(type(y)) #type() funkcija datu tipa noteikšanai

vards = "Anna"
uzvards = "Bērziņa" #starp pēdiņām var likt jebkādus simbolus, tai skaitā ar mīkstinājuma zīmēm un garumzīmēm

print(vards)
print(uzvards)

#Izvadīt tekstu vienā rindā
#1.veids
print(vards+uzvards)
#2.veids
z = vards+' '+uzvards
print(z)
#3.veids
print(vards,uzvards)

#Teksta garums
#len() - funkcija simbolu skaita noteikšanai
print(len(vards))
print(len(uzvards))

#Piekļuve atsevišķiem teksta elementiem
#indeksēšana - sākas no 0

#Atsevišķa elementa izvade
print(vards[3]) #izvadīsim vārda Anna pēdējo burtu
#print(vards[4]) #error: string index out of range

#Vairāku elementu izvade
print(uzvards[:3]) #no pirmā elementa līdz trešajam (trešo neieskaitot)
print(uzvards[1:5]) 

#Izvadīt pēdējo elementu, nezinot viņa indeksu
print(uzvards[-1])

#Izvadīt elementus ar soli 1
print(uzvards[::1])
#Izvadīt elementus ar soli 2
print(uzvards[::2])

#Apgriezt tekstu otrādi
print(uzvards[::-1])

#Mainīt mainīgā vērtību
vards = "Cecīlija"
uzvards = uzvards + "-Liepa"
print(vards,uzvards)

#Datu tipa String metodes

#.upper() - pārveido visus burtus par lieliem burtiem
print(vards.upper())
#.lower() - pārveido visus burtus par maziem burtiem
print(vards.lower())
#.split() - sadala tekstu, pēc noklusējuma dala tur, kur ir atstarpes
print(uzvards.split())
print(uzvards.split("-"))

print("Cecīlija\n"+uzvards)