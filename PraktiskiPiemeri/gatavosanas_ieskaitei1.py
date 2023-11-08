"""
Gatavošanās ieskaitei

08.11.2023
"""


#1.uzdevums

#Izveido sarakstu ar trīs elementiem, kuriem ir atšķirīgi datu tipi

#Saraksta konstrukcija
# mainigaNosaukums = [elements1,elements2,elements3........]

# saraksts = [4,6.7,"Sveiki"]


#2.uzdevums

#Izveido funkciju SveikaPasaule, kas izvada tekstu "Sveika, Pasaule!"

#Konstrukcija
#def funkcijasNosaukums():
#   funkcijas saturs

def SveikaPasaule():
    print("Sveika, Pasaule!")
    
SveikaPasaule()


#3.uzdevums

# Uzraksti funkciju, kura atgriež mazāko skaitli, ja abi skaitļi ir pāra skaitļi
# Atgriež lielāko skaitli, ja abi skaitļi ir nepāra vai viens no skaitļiem ir nepāra skaitlis

"""
print(funkcijasNosaukums(2,4)) -----> 2
print(funkcijasNosaukums(2,5)) -----> 5
"""
#Funkcija atgiezSkaitli(skaitlis1,skaitlis2)
def atgriezSkaitli(skaitlis1,skaitlis2):
    
    #Pārbaude - vai pirmais skaitlis ir pāra skaitlis
    if skaitlis1 % 2 == 0:
        #Pārbaude - vai otrais skaitlis ir pāra skaitlis
        if skaitlis2 % 2 == 0:
            #Pārbaude - kurš no skaitļiem ir mazāks
            if skaitlis1<skaitlis2:
                return skaitlis1
            else:
                return skaitlis2
        #Ja skaitlis2 nav pāra skaitlis
        else:
            #Pārbaude - kurš no skaitļiem ir lielāks
            if skaitlis1>skaitlis2:
                return skaitlis1
            else:
                return skaitlis2
    #Ja skaitlis1 nav pāra skaitlis
    else:
        #Pārbaude - kurš no skaitļiem ir lielāks
        if skaitlis1>skaitlis2:
            return skaitlis1
        else:
            return skaitlis2
        
# print(atgriezSkaitli(2,4))
# print(atgriezSkaitli(2,5))
print(atgriezSkaitli(1,5))


#Funkcija atgiezSkaitli(skaitlis1,skaitlis2)
def atgriezSkaitli(skaitlis1,skaitlis2):
    
    #Pārbaude - vai pirmais un otrais skaitlis ir pāra skaitļi
    if skaitlis1 % 2 == 0 and skaitlis2 % 2 == 0:
        #Pārbaude - kurš no skaitļiem ir mazāks
        if skaitlis1<skaitlis2:
            return skaitlis1
        else:
            return skaitlis2
    #Ja skaitlis1 un skaitlis2 nav pāra skaitļi
    else:
        #Pārbaude - kurš no skaitļiem ir lielāks
        if skaitlis1>skaitlis2:
            return skaitlis1
        else:
            return skaitlis2
        
print(atgriezSkaitli(2,4))
print(atgriezSkaitli(2,5))
print(atgriezSkaitli(1,5))


#Funkcija atgiezSkaitli(skaitlis1,skaitlis2)
def atgriezSkaitli(skaitlis1,skaitlis2):
    
    #Pārbaude - vai pirmais un otrais skaitlis ir pāra skaitļi
    if skaitlis1 % 2 == 0 and skaitlis2 % 2 == 0:
        #Pārbaude - kurš no skaitļiem ir mazāks, izmantojot iebūvētās funkcijas
        return min(skaitlis1,skaitlis2)
    #Ja skaitlis1 un skaitlis2 nav pāra skaitļi
    else:
        #Pārbaude - kurš no skaitļiem ir lielāks
        return max(skaitlis1,skaitlis2)
        
print(atgriezSkaitli(2,4))
print(atgriezSkaitli(2,5))
print(atgriezSkaitli(1,5))
