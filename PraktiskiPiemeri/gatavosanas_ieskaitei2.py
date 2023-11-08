"""
Treniņš programmas veidošanai pēc specifikācijas
"""

#1.specifikācija

"""
Uzraksti funkciju:
*ievadīt linoleja cenu
*ievadīt telpas izmēru
*izvadīt cenu
"""

def telpasIzmers(cena,izmers):
    kopeja_cena = cena *izmers
    
    print("Grīdas seguma kopējā cena: ",kopeja_cena)
    
telpasIzmers(5,20)
