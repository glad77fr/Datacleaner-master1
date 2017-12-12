from openpyxl import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import numpy as np

# wb = Workbook()

# root = tk.Tk()
# root.withdraw()  # pour ne pas afficher la fenêtre Tk

# path = askopenfilename()  # lance la fenêtre et recupère le chemin

# wb = load_workbook(path)
# ws = wb.active

# c = ws['B3']
# lol
class Analyse:
    "Classe permettant d'effectuer des contrôles de qualité sur des données"

    def __init__(self):
        self.localisation = " "
        self.wb = Workbook()
        self.Excel = pd.ExcelFile(r'C:\Users\Sabri.GASMI\Desktop\Jeu.xlsx')  # Chargement du fichier excel
        #self.Excel.parse(convert_float=false)
        self.df = self.Excel.parse('Feuil1')

        # df = xls_file.parse('Feuil1')
        # for cel in df['Nom']:
        # if cel[0] == 'A':
        # print(cel)

    def charger(self):
        root = tk.Tk()
        root.withdraw()
        self.localisation = askopenfilename()
        print(self.localisation)

    def vide(self,champs):
        "Méthode permettant de vérifier si une colonne est vide"
        n = 1
        for cel in self.df[champs]:
            if pd.isnull(cel):
                print(n)
            n += 1


toto = Analyse()
toto = Analyse.vide(toto,'Nom')
help(Analyse)