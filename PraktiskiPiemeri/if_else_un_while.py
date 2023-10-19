"""
Praktisks piemērs while cikla un apgalvpjumu izmantošanai
Vai ir ievadīta pareiza parole?
"""
print("Lūdzu izveido savu paroli:")
parole = input()

while True: #True - boolean vērtība, kura visu laiku patiesa, līdz to pārtrauc
    
    print("Ievadi paroli atkārtoti:")
    parole2 = input()

    if parole2==parole:
        break

print("Paldies, tava parole ir izveidota")

