"""
Excel datnes apstrāde un izveidošana
"""
import xlwt  #Faila izviedei un rediģēšanai
import xlrd  #Faila nolasīšanai

darbaGramata = xlrd.open_workbook('Excel_piemers.xls')
lapa = darbaGramata.sheet_by_index(0)

for rinda in lapa:
    print(rinda)
    print(type(rinda))

jaunaDarbaGramata = xlwt.Workbook()
jaunaLapa = jaunaDarbaGramata.add_sheet('Lapa 1')

#Vērtību ierakstīšanai ir jāzina šūnas adrese
for x in range(1,11):
    for y in range(1,11):
        jaunaLapa.write(x-1,y-1,x*y)

jaunaDarbaGramata.save("JaunaDarbaGramata.xls")
