"""
Uzraksti funkciju, kura atgriež vērtību True, ja abi dotie vārdi sākas ar vienu burtu.

print(sakas_vienadi("Liela Lama")) -----> True
print(sakas_vienadi("Maza Lama")) ------> False
"""
teksts = "Liela Lama"
print("Funkcija, kas der tikai Liela Lama tekstam")
def sakas_vienadi(teksts):
    #Indeksēšana a = "abc"
    #print(a[1])
    
    pirmaisBurts = teksts[0]
    otraisBurts = teksts[6]
    
    if pirmaisBurts == otraisBurts:
        return True
    else:
        return False
    
    return pirmaisBurts,otraisBurts
    
    
print(sakas_vienadi(teksts))
print("Funkcija ar atdalītiem vārdiem")
def sakas_vienadi(teksts):
    #.split() - metode teksta sadalīšanai, teksts tiek pārveidots par sarakstu (list)
    sadalitsTeksts = teksts.split() #pēc noklusējuma dala tur, kur ir atstarpes
    print(sadalitsTeksts)
    
    if sadalitsTeksts[0][0] == sadalitsTeksts[1][0]:
        print(sadalitsTeksts[0][0])
        return True
    else:
        return False
    
print(sakas_vienadi("Liela Lama"))    
print(sakas_vienadi("Maza Lama"))

print(sakas_vienadi("Liela lama"))    
print(sakas_vienadi("Maza Mama"))

print("Funkcija ar samazinātiem burtiem un atdalītiem vārdiem")
def sakas_vienadi(teksts):
    #.lower() - samazina visus burtus
    #.upper() - palieliena visus burtus
    samazinatsTeksts = teksts.lower()
    sadalitsTeksts = samazinatsTeksts.split()
    
    if sadalitsTeksts[0][0] == sadalitsTeksts[1][0]:
        return True
    else:
        return False
    
print(sakas_vienadi("lIELA Lama"))

print("Īsākais pieraksta veids")
def sakas_vienadi(teksts):
    sarakstsSalidzinasanai = teksts.lower().split()
    
    return sarakstsSalidzinasanai[0][0] == sarakstsSalidzinasanai[1][0]

print(sakas_vienadi("lIELA Lama"))

print("Īsākais pieraksta veids - VĒL ĪSĀKS")
def sakas_vienadi(teksts):
    
    return teksts.lower().split()[0][0] == teksts.lower().split()[1][0]

print(sakas_vienadi("lIELA Lama"))
