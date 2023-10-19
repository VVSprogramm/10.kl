#for cikls
#for - cikls

#for - kaut kas, ko var saskaitīt

#konstrukcija
#for ciklaMainigais in nosacijums:   #for in 
#    cikla ķermenis

masinas = ['Audi','BMW','WW','Opel'] #saraksts - list
print(masinas[0])
print(masinas[1])
print(masinas[2])
print(masinas[3])

print(len(masinas))

#1.ietrācija: masina = 0 
#    masinas[0]
#2.ietrācija: masina = 1 
#    masinas[1]
#3.ietrācija: masina = 2
#    masinas[2]
#4.ietrācija: masina = 3 
#    masinas[3]

print("\n Pirmais for cikls")
for masina in range(len(masinas)): #range() - 0,sarakstaGarumam
  print(masinas[masina])

print("Pirmais for cikls beidzās \n")


#1.iterācija: masina 
for masina in masinas:
  print(masina)

print("For cikls beidzās")


#Uzdevuma piemērs
#1.Veido for ciklu, definējot loģisku elementa nosaukumu un ievietojot iepriekš
#izveidoto sarakstu- 0.4p
#2.Veido cikla ķermeni, izvadi tekstu "Sveika, Pasaule!" (print funkcija)- 0.4p

a = ["b","b","b","c","a","t"] #saraksts
for tekstaMainigais in a:
  print("Sveika, Pasaule!")