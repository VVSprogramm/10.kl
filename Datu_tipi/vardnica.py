"""
Datu tips
vardnica - dictionary
"""

pirmais = {'atsl1':'vertiba1'
,
'atsl2':'vertiba2'}

print(pirmais)
#Izvadīt konkrētu vērtību, tā tiek pēc atslēgas
print("Pirmās atslēgas vērtība: ",pirmais['atsl1'])

#Atslēga vienmēr ir pēdiņās, bet tā neskaitās kā dati
otrais = {'atsl1':'vertiba1','atsl2':2.5,'atsl3':[1,2,3],'atsl4':{'atsl5':[2,5,7]}}
#'atsl1':'vertiba1' - tiek glabāti teksta dati
#'atsl2':2.5 - tiek glabāti decimāldaļas
#'atsl3':[1,2,3] - tiek glabāts saraksts
#'atsl4':{'atsl5':[2,5,7]} - tiek glabāta vārdnīca 
print(otrais)
print(otrais['atsl3'])

d = {}
d['vards']='Anna'
print(d)
d['vecums']=25
print(d)

print(pirmais.keys())
print(pirmais.values())
print(pirmais.items())