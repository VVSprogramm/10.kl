"""
Teksta dokumentu atvēršana un nolasīšana (txt formāts)
31/01/2023
"""

#1. atvēršanas veids

fails = open("Datnes/lasit.txt","r", encoding="UTF-8") #r - lasīšanas stāvoklis, "UTF-8" - priekš specifisku simbolu nolasīšanas
print(fails.read()) #Faila satura lasīšana un izvadīšana
fails.close() #Faila aizvēršana

# 2.atvēršanas veids

with open("Datnes/lasit.txt","r", encoding="UTF-8") as fail:
    print(fail.read())


#Faila rindu lasīšana

with open("Datnes/lasit.txt","r", encoding="UTF-8") as fail:
    print(fail.readlines())

    #Rezultāts
    #['Šodien ir trešdiena. \n', 'Drīz beigsies stundas.\n']
    #\n - pārnešana jaunā rindā

    #Jautājums:
    #Kāds datu tips ir izvadē?
    print(type(fail.readlines())) #Tā var noskaidrot atbildi

#Datu saglabāšana
#Jāatceras, ka lasot failu, mēs pārvietojamies failā uz priekšu
with open("Datnes/lasit.txt","r", encoding="UTF-8") as fail: 
    
    #Lai saglabātu datus
    dati = fail.readlines()
    print(dati[1])
    print(dati[0])
    dati2 = fail.readlines()
    print(dati2)
    print(dati)

#Faila rindas lasīšana
with open("Datnes/lasit.txt","r", encoding="UTF-8") as fail:
    print(fail.readline())
    print(fail.readline())
    print(fail.readline())

#Lasīt konkrētu simbolu skaitu
with open("Datnes/lasit.txt","r", encoding="UTF-8") as fail:
    print(fail.read(15))



#Jauna teksta faila veidošana
    
jaunsFails = open("Datnes\JaunsIzmeginajumaFails.txt","w",encoding="UTF-8")
#jaunsFails.write("Sanāca izveidot jaunu failu, juhuuuuuuuu!")
saturs = "Iepriekš sagatavota teksta saglabāšana teksta failā.\nŠis teksts būs jaunā rindā."
jaunsFails.write(saturs)
vards="Janīna"
vecums = 15
skola = "Viļānu vidusskola"
saturs2 = "\n"+vards+str(vecums)+skola
print(type(saturs2))
jaunsFails.write(saturs2)
saturs3 = ["\n"+vards+"\n",str(vecums)+"\n",skola]
jaunsFails.writelines(saturs3)
jaunsFails.close()

with open("Datnes\JaunsIzmeginajumaFails.txt","r", encoding="UTF-8") as JaunsFailsLasit:
    print(JaunsFailsLasit.read())

with open("Datnes\JaunsIzmeginajumaFails.txt","w", encoding="UTF-8") as JaunsFailsRakstit:
    print(JaunsFailsRakstit.write("Nekā nebija. "))

with open("Datnes\JaunsIzmeginajumaFails.txt","r", encoding="UTF-8") as JaunsFailsLasit:
    print(JaunsFailsLasit.read())

with open("Datnes\JaunsIzmeginajumaFails.txt","a", encoding="UTF-8") as JaunsFailsRakstitKlat:
    print(JaunsFailsRakstitKlat.write("Es esmu klāt!"))

with open("Datnes\JaunsIzmeginajumaFails.txt","r", encoding="UTF-8") as JaunsFailsLasit:
    print(JaunsFailsLasit.read())