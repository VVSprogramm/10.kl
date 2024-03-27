""" 
Datu validācija
"""

#Pārbaude, vai lietotājs ievada to, ko mēs sagaidām
#Karodziņa izveide
ir_skaitlis = False

while ir_skaitlis==False:
    lietotaja_ievade = input("Lūdzu, ievadi savu dzimšanas gadu: ")

    if lietotaja_ievade.isnumeric() == True: #Metode, kas pārbauda vai mainīgais ir skaitlis
        # vecums = 2024-int(lietotaja_ievade)
        # print("Tavs vecums ir: ",vecums)
        ir_skaitlis=True
    else:
        print("Tu neievadīji gadu, lūdzu, mēģini vēlreiz!")

vecums = 2024-int(lietotaja_ievade)
print("Tavs vecums ir: ",vecums)


#Reģistrācijas process

print("Lai lietotu šo programmu, nepieciešams reģistrēties, lūdzu, seko norādījumiem zemāk:")
lietotaj_vards = input("Lūdzu, ievadi savu vēlamo lietotājvārdu: ")

while True:
    parole = input("Lūdzu ievadi savu paroli (tai jābūt vismaz 8 simbolus garai): ")
    print(len(parole))

    if len(parole) >= 8:
        break
    else:
        print("Ievadītajā parolē ir mazāk kā 8 simboli")

print("Paldies par reģistrāciju!")
