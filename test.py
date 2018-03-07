import pandas as pd
from xlsxwriter import *

a = pd.DataFrame({'Maison': ["Rouge", "Jaune"], 'Chien': ["Vilain", "cool"]})

print(a)
print(a.columns.isin(['ff']))

def titi(a):
    print(a)

def toto(b):
    print(b.upper())
#exec('titi(3)')

#exec("toto(\'lol\')")

