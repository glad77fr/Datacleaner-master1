from openpyxl import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import sys as syst


class Analyse:
    """Classe permettant d'effectuer des contrôles de qualité sur des données"""

    def __init__(self):
        self.localisation = " "
        self.wb = Workbook()
        # self.Excel = pd.ExcelFile(r'C:\Users\Sabri.GASMI\Desktop\Jeu.xlsx')  # Chargement du fichier excel
        #self.Excel = pd.ExcelFile(r'C:\Users\Sabri\Desktop\Test.xlsx')
        self.Excel = pd.ExcelFile(r'/Users/sabrigasmi/Desktop/Effectif.xlsx')
        self.df = self.Excel.parse('Feuil1')
        self.dfr = pd.DataFrame()  # Stock les réponses
        # print(self.df.iloc[:,0])
        self.dfr['Matricule_sal'] = self.df.iloc[:, 0]  # Ajoute le matricule au fichier résultat
        self.dfr['Nom_sal'] = self.df.iloc[:, 1]  # Ajoute les noms au fichier résultat
        self.dfr['Prénom_sal'] = self.df.iloc[:, 2]  # Ajoute les noms au fichier résultat

    def charger(self):
        root = tk.Tk()
        root.withdraw()
        self.localisation = askopenfilename()
        print(self.localisation)

    def vide(self, champs):
        """"Méthode permettant de vérifier si une cellule est vide"""
        self.__check_variable(champs)
        resultat = []
        n = 2

        for cel in self.df[champs]:
            if pd.isnull(cel):
                resultat.append(n)
            n += 1
        self.charg_result(champs, resultat, 'champ vide')
        print(resultat)

    def espace(self, champs):
        """Méthode permettant de vérifier si une cellule comporte des espaces en début de chaine"""
        self.__check_variable(champs)
        resultat = []
        stockage_str = []
        n = 2
        stockage_str = self.df[champs].astype(str)
        for cel in stockage_str:
            if cel[0] == " ":
                resultat.append(n)
            n += 1
        self.charg_result(champs, resultat, 'Espace devant le champ')
        print(resultat)

    def doublon(champs):
        """Méthode permettant de vérifier si une donnée est dupliquée"""
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

    def charg_result(self, champs, liste, anomalie):
        """Permet de charger les résultats dans le dataframe"""
        if len(liste) != 0:  # vérifie que la liste de résultat n'est pas vide, sinon on s'arrête
            if champs in self.dfr.columns:# Vérifie si le champs existe déjà dans les résultats
                n = 0
                for ch in self.dfr.columns:  #Détermine la position du champ existant dans le résultat
                    if ch != champs:
                        n += 1
                i = 0
                for cel in liste: #Détermine si le champ est vide, si oui on remplace 'NaN' par le résultat
                    if str(self.dfr.iloc[i, n]) != 'nan':
                        self.dfr.at[liste[i], champs] = str(self.dfr.iloc[i, n]) + anomalie
                        i += 1
                    else:
                        self.dfr.at[liste[i], champs] = anomalie
            else: #Si le champs n'existe pas, on va le créer dans résultat
                self.dfr.assign(champs="")
                i = 0
                for scel in liste:
                    self.dfr.at[liste[i], champs] = anomalie
                    i += 1
            #print(self.dfr.columns)

    def __check_variable(self, champs):
        """Méthode interne permettant de vérifier si un champ existe"""
        for ch in self.df.columns:
            if ch == champs:
                res = True
        if not res:
            print("Champ inexistant dans le fichier")
            syst.exit()


toto = Analyse()

# toto.vide('Nom')
toto.espace('Site')
toto.vide('Site')
print(toto.dfr)

#toto.vide('Statut')


# toto = Analyse.vide(toto,'Nom')
# help(Analyse) fr
