"""
05.10.2023.
Datu tipi
Saraksts - list
"""

masinas = ['Audi','BMW','WW','Opel']

print("Saraksta masinas izvade: ",masinas) #Saraksta izvade

#indeksēšana
vards = "Anna"
print(vards[1])

print("Saraksta masinas pirmā elementa izvade",masinas[0])


saraksts1 = ['Anna',5,4.2,[5,6,'Pēteris']]
print(saraksts1)
print("Ceturtais elements:",saraksts1[3])
print("Ceturtā elementa trešais elements: " + saraksts1[3][2]) #indekss 3 apzīmē saraksta 4 elementu, otrs indekss 2 ļauj izvadīt
produkti = ['Piens'
,
'Maize'
,
'Olas']
produkti[1] = "Lavašs" #Elementa nomaiņa sarakstā
print(produkti)

#print(produkti.len()) Dotais kods nestrādāja

print(len(produkti))

produkti.append("Maize")
print(produkti)

produkti.pop(1)
print(produkti)