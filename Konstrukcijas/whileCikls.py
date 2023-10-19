# while - tas nozīmē, ka ir cikls
# while nosacījums:
#    cikla ķermenis (darbības, kas tiks izpildītas)
#print("Cikla beigas")

#while cikls tiek izmantots, ja nav zināms, cik tieši reizes darbībai ir jāatkārtojas

cipars  = 5 #vesels skaitlis integer

#1.cikls - cipars = 5
#     5-1=4
#2.cikls - cipars = 4
#     4-1=3
#3.cikls - cipars = 3
#     3-1=2
#4.cikls - cipars = 2
#     2-1=1
#5.cikls - cipars = 1
#     1-1=0


while cipars>0: #nosacījums
  print("Esam ciklā") #cikla ķermenis
  cipars = cipars - 1
  print("Cikla skaitlis:",cipars)

#Ārpus cikla
print("Cikls ir beidzies")


#boolean - datu tips
#karodziņiem

# paroleIrPareiza = False #zaļš vai sarkans

# while paroleIrPareiza:
#   print("Ievadi paroli: ")
#   print("Parole: 1234")
#   paroleIrPareiza = False
