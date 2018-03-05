#from openpyxl import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import sys as syst
from xlsxwriter import *


class Analyse:
    """Classe permettant d'effectuer des contrôles de qualité sur des données"""

    def __init__(self):
        self.localisation = " "
        self.wb = Workbook()
        #self.Excel = pd.ExcelFile(r'C:\Users\Sabri.GASMI\Desktop\Jeu.xlsx')  # Chargement du fichier excel
        # self.Excel = pd.ExcelFile(r'C:\Users\Sabri\Desktop\Test.xlsx')
        #self.Excel = pd.ExcelFile(r'/Users/sabrigasmi/Desktop/Effectif.xlsx')
        self.Excel = pd.ExcelFile(r'D:\Users\sgami\Desktop\Test.xlsx')
        self.df = self.Excel.parse('Test')
        self.dfr = pd.DataFrame()  # Stock les réponses dans un dataframe
        self.dfr['Matricule_sal'] = self.df.iloc[:, 0]  # Ajoute le matricule au fichier résultat
        self.dfr['Nom_sal'] = self.df.iloc[:, 1]  # Ajoute les noms au fichier résultat
        self.dfr['Prénom_sal'] = self.df.iloc[:, 2]  # Ajoute les noms au fichier résultat

    def charger(self):
        root = tk.Tk()
        root.withdraw()
        self.localisation = askopenfilename()
        print(self.localisation)

    def vide(self, champs, line=None):
        """"Méthode permettant de vérifier si une cellule est vide"""
        self.__check_variable(champs)  # Verification que le champ existe dans le fichier

        if line is None:  # Check que l'option line n'est pas activée
            resultat = []
            n = 0

            for cel in self.df[champs]:
                if pd.isnull(cel):
                    resultat.append(n)
                n += 1
            self.charg_result(champs, resultat, 'champ vide')
        else:
            if str(self.df.at[line, champs]) == "nan":
                return True

            else:
                return False

    def espace(self, champs, line=None):
        """Méthode permettant de vérifier si une cellule comporte des espaces en début de chaine"""
        self.__check_variable(champs)

        if line is None:
            resultat = []
            n = 0
            stockage_str = self.df[champs].astype(str)
            for cel in stockage_str:
                if cel[0] == " ":
                    resultat.append(n)
                n += 1

        else:
            stockage_str = str(self.df.at[line, champs])
            if stockage_str[0] == " ":
                return True, print(stockage_str)

            else:
                return False
        self.charg_result(champs, resultat, 'Espace devant le champ')

    def doublon(self, champs1):
        """Méthode permettant de vérifier si une donnée est dupliquée"""
        self.__check_variable(champs1)  # Verification que le champ existe dans le fichier
        n = 0
        resultat = []

        for cel in self.df[champs1]:
            occ = 0
            if n != 0:
                for ligne in self.df[champs1]:
                    if ligne == cel:
                        occ += 1
            if occ > 1:
                resultat.append(n)
            n += 1
        self.charg_result(champs1, resultat, 'Doublon')

    def charg_result(self, champs=None, liste=None, anomalie=None):
        """Permet de charger les résultats dans un dataframe"""

        if len(liste) != 0:  # vérifie que la liste de résultat n'est pas vide, sinon on s'arrête
            if champs in self.dfr.columns:  # Vérifie si le champs existe déjà dans les résultats
                n = 0
                for ch in self.dfr.columns:  # Détermine la position du champ existant dans le résultat
                    if ch != champs:
                        n += 1
                i = 0
                for cel in liste:  # Détermine si le champ est vide, si oui on remplace 'NaN' par le résultat
                    if str((self.dfr.at[liste[i], champs])) == 'nan':
                        self.dfr.at[liste[i], champs] = anomalie
                    else:
                        self.dfr.at[liste[i], champs] = str(self.dfr.iloc[i, n]) + " " + anomalie
                    i += 1

            else:  # Si le champs n'existe pas, on va le créer dans résultat
                self.dfr.assign(champs="")
                i = 0
                for cel in liste:
                    self.dfr.at[liste[i], champs] = anomalie
                    i += 1

    def __check_variable(self, champs):
        """Méthode interne permettant de vérifier si un champ existe"""
        res = False
        for ch in self.df.columns:
            if ch == champs:
                res = True
        if not res:
            print("Erreur, le champs " + champs + " est inexistant dans le fichier")
            syst.exit()

    def exportexcel(self, repertoire, onglet):
        """Méthode permettant d'extraire le résultat sous forme d'un fichier excel"""
        writer = pd.ExcelWriter(repertoire, engine='xlsxwriter')
        self.dfr.to_excel(writer, sheet_name=onglet)
        writer.save()


toto = Analyse()
#toto.espace('Prénom')
toto.espace('Prénom')
#toto.vide('Prénom')
#print(toto.espace('Prénom', 3))
#print(toto.vide('Code Analytique',0))
#toto.vide('Site',2)
toto.exportexcel(r'D:\Users\sgami\Desktop\resultat.xlsx', 'toto')

#toto.doublon('Site')
#print(toto.dfr)

# toto.vide('Statut')

# toto = Analyse.vide(toto,'Nom')
# help(Analyse) fr
