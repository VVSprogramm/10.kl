# Izveido funkciju summa() ar diviem parametriem - skaitlis1 un skaitlis2, 
#kas izvada tekstu "IR", ja abu skaitļu summa ir 20, visos citos gadījumos izvada tekstu "NAV".

# summa(10,10) ------ > IR
# summa(10,20) ------ > NAV
# summa(5,15) ---------> IR


def summa(skaitlis1,skaitlis2):
    if skaitlis1 + skaitlis2 == 20:
        print("IR")
    else:
        print("NAV")

summa(10,10)
summa(10,20)
summa(5,15)



  