import pandas as pd
from xlsxwriter import *


def titi(a):
    print(a)

def toto(b):
    print(b.upper())
exec('titi(3)')

exec("toto(\'lol\')")

