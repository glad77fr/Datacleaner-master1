from openpyxl import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import numpy as np


class Analyse:
    "Classe permettant d'effectuer des contrôles de qualité sur des données"

    def __init__(self):
        self.localisation = " "
        self.wb = Workbook()
        self.Excel = pd.ExcelFile(r'C:\Users\Sabri.GASMI\Desktop\Jeu.xlsx')  # Chargement du fichier excel
        #self.Excel.parse(convert_float=false)
        self.df = self.Excel.parse('Feuil1')
        self.dfr = pd.DataFrame() # Stock les réponses
        print(self.df.iloc[:,0])

    def charger(self):
        root = tk.Tk()
        root.withdraw()
        self.localisation = askopenfilename()
        print(self.localisation)

    def vide(self,champs):
        "Méthode permettant de vérifier si une cellule est vide"
        n = 1
        for cel in self.df[champs]:
            if pd.isnull(cel):
                print(n)
            n += 1
    def espace(self,champs):
        "Méthode permettant de vérifier si une cellule comporte des espaces en début de chaine"
        n = 1
        self.df[champs] = self.df[champs].astype(str)
        for cel in self.df[champs]:
                if cel[0] == " ":
                    print(n)
                n += 1

    def doublon(self,champs):
        "Méthode permettant de vérifier si une donnée est dupliquée"
        n = 1
        o = 0
        for cel in self.df[champs]:
                o = 0
                valrech = cel
                for val in self.df[champs]:
                    if valrech == val:
                        o += 1
                print(self.df['Nom'][n], ' ', o)
                n += 1

toto = Analyse()
toto.espace('Nom')
#toto = Analyse.vide(toto,'Nom')
#help(Analyse)

