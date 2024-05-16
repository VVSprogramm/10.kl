import sys


try:
    print(5/0)
except:
    print("Kļūda: ",sys.exc_info()[0])


print(5/0)