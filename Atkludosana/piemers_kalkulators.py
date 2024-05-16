"""
Kalkulators
"""
import csv #Ievietota bibliotēka

#Funkcijas def veic matemātiskas darbības
def saskaitisana(x, y):
    return x + y
def atnemsana(x, y):
    return x - y
def reizinasana(x, y):
    return x * y
def dalisna(x, y):
    return x / y 

#funkcija datu saglabāšanai
def datu_saglabasana(vards,rezultats):
    saturs = [vards,rezultats]
    with open("kalkulatora_dati.csv","a", encoding="UTF-8") as fails: #Notiek datu pievienošana
        csvwrite = csv.writer(fails) #Objekta izveide
        csvwrite.writerow(saturs)

#funkcija skaitļa pārbaudei
def ievades_skaitla_parbaude():
    ievade = (input("Ievadi skaitli: "))
    while True:
        if ievade.isnumeric():
            num = float(ievade)
            break
        else:
            ievade = (input("Ievadi skaitli: ")) 
    return num


vards = input("Lūdzu ievadi savu vārdu: ")

#Cikls nodrošina programas darbību
while True:

    izvele = input("Izvēlaties darbību(+, -, *, /): ") #Lietotāja darbības izvēle
    
    darbibas = ["+","-","*","/"]
    vai_sakrit = []
    while True:
        for i in darbibas:
            if izvele == i:
                vai_sakrit.append(izvele)
        if len(vai_sakrit) < 1:
            izvele = input("Izvēlaties darbību(+, -, *, /): ")
        else:
            break

    #Skaitļu ievade
    print("Pirmais skaitlis")
    num1 = ievades_skaitla_parbaude()
    print("Otrais skaitlis")
    num2 = ievades_skaitla_parbaude()

    #Lietotāja izvēlētās darbības pārbaude, darbības izpilde un datu saglabāšana
    if izvele == "+":
        rezultats = saskaitisana(num1, num2)
        print('The summa {0} and {1} is {2}'.format(num1, num2, rezultats))
        datu_saglabasana(vards,rezultats)

    if izvele == "-":
        rezultats = atnemsana(num1, num2)
        print('The starpība {0} and {1} is {2}'.format(num1, num2, rezultats))
        datu_saglabasana(vards,rezultats)

    if izvele == "*":
        rezultats = reizinasana(num1, num2)
        print('The reizinājums {0} and {1} is {2}'.format(num1, num2, rezultats))
        datu_saglabasana(vards,rezultats)
    if izvele == "/":

        rezultats = dalisna(num1, num2)
        print('The dalījums {0} and {1} is {2}'.format(num1, num2, rezultats))
        datu_saglabasana(vards,rezultats)

    #Lietotājs izvēlās vai vēlās turpināt turpmākās darbības      
    while True:
        jautajums = input("Vai veiksim turpmākās darbības? (Jā/Nē): ")

        if jautajums == "Nē": 
            print("Paldies, ka izmantoji manu kalkulatoru!")
            exit()
        if jautajums == "Jā":
            print("Sākam no jauna!")
            break
        else:
            print("Ievadi savu izvēli vēlreiz")
    