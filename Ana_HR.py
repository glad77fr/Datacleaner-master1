from openpyxl import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import petl as petl


class Analyse:
    "Classe permettant d'effectuer des contrôles de qualité sur des données"

    def __init__(self):
        self.localisation = " "
        self.wb = Workbook()
        self.Excel = pd.ExcelFile(r'C:\Users\Sabri.GASMI\Desktop\Jeu.xlsx')  # Chargement du fichier excel
        self.df = self.Excel.parse('Feuil1')
        self.dfr = pd.DataFrame() # Stock les réponses
        #print(self.df.iloc[:,0])
        self.dfr['Matricule_sal'] = self.df.iloc[:,0] # Ajoute le matricule au fichier résultat
        self.dfr['Nom_sal'] = self.df.iloc[:, 1] #Ajoute les noms au fichier résultat
        self.dfr['Prénom_sal'] = self.df.iloc[:, 2]  # Ajoute les noms au fichier résultat

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
        resultat=[]
        n = 2
        self.df[champs] = self.df[champs].astype(str)
        for cel in self.df[champs]:
                if cel[0] == " ":
                    resultat.append(n)
                n += 1
        #print(resultat)
        self.charg_result(champs, resultat, 'Espace devant le champ')

    def doublon(champs):
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

    def charg_result(self,champs,liste,anomalie):
        "Permet de charger les résultats dans le dataframe"
        if len(liste) != 0:
            if champs in self.dfr.columns:
                print("champ inexistant")
            else:
                self.dfr.assign(champs="")
                i = 0
                for cel in liste:
                    print(liste.index(cel))
                    self.dfr.at[liste[i],champs] = anomalie
                    i += 1
            print(self.dfr.columns)

toto = Analyse()

#toto.vide('Nom')
toto.espace('Nom')
#toto = Analyse.vide(toto,'Nom')
#help(Analyse) f

