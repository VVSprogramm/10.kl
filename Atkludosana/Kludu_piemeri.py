# #Nokopē kodu, atrodi risinājumu un pieraksti kļūdas veidu

# # Lietotājs ievada divus veselus skaitļus a un b. Izvadi visus skaitļus šajā intervālā (ieskaitot)!

# a = int(input("Ievadi a:"))
# b = int(input("Ievadi b:"))

# for i in range(a, b):
#   print(i)

# #Kļūdas veids - NameError
# #Risinājums - sestajā rindā mainīgā nosaukums no a, jānomaina uz b



# #Nokopē kodu, atrodi risinājumu, pieraksti kļūdas veidu un apraksti risinājumu

# # Lietotājs ievada veselu pozitīvu skaitli. Izdrukā visus skaitļus sākot no ievadītā līdz 0 (neieskaitot)!

# sk = int(input("Ievadi skaitli:"))
# while sk > 0:
#   print(sk)
#   sk -= 1


# Lietotājs ievada vairākus skaitļus vienā rindā, atdalot tos ar atstarpi. Izvadi tos skaitļus, kuri ir vienādi un atrodas blakus!

# saraksts = [int(sk) for sk in input("Ievadi skaitlus, atdalot tos ar atstarpi:").split()]

# for i in range(len(saraksts)-1):
#     if saraksts[i] == saraksts[i + 1]:
#         print(saraksts[i], saraksts[i + 1])


# Lietotājs ievada vairākus skaitļus, atdalot tos ar atstarpi. Izvadi lielākā ievadītā skaitļa vērtību un indeksu sarakstā!

skaitli = [int(skaitli) for skaitli in input("Ievadi skaitlus, atdalot tos ar atstarpi:").split()]

lielIndex = 0

for i in range(1, len(skaitli)):
  if skaitli[i] > skaitli[lielIndex]:
    lielIndex = i

#mainīgās vērtības ievietošana tesktā
#f, kur priekšā tekstam liek f un starp tekstu figūriekavās norāda mainīgo, kura vērtība ir jāievieto
print(f"Lielakais skaitlis: {skaitli[lielIndex]} ar indeksu {lielIndex}")

      