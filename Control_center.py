import pandas as pd
import Simple_control as sp
import time
import Complex_control as cp


class Control_center:
    def __init__(self, path_datasource, worksheets):
        self.path_datasource = path_datasource  # containing the path of the datasource
        self.datasource = pd.DataFrame()    # DataFrame containing the analysed dataset
        self.bool_result = pd.DataFrame()   # DataFrame containing the boolean result
        self.text_result = pd.DataFrame()    # DataFrame containing the commented result
        self.worksheets = worksheets    # worksheets of the Excel source file
        self.__load_excel_datasource()  # transfer of the excel file containing data to source DataFrame

    def __load_excel_datasource(self):

        try:
            self.Excel = pd.ExcelFile(self.path_datasource)
            self.datasource = self.Excel.parse(self.worksheets)
        except:
            print("the excel file doest exist")

    def first_raws(self, *args):
        nb = 0
        try:
            for arg in args:
                self.bool_result[arg] = self.datasource[arg]
                self.text_result[arg] = self.datasource[arg]
                nb += 1
        except:
            print("the column doest exist")

        if nb != 0:
            cols = self.bool_result.columns.tolist()
            cols = cols[-nb:] + cols[:nb]
            self.bool_result = self.bool_result[cols]
            cols = self.text_result.columns.tolist()
            cols = cols[-nb:] + cols[:nb]
            self.text_result = self.text_result[cols]

    def empty(self, column_name, showed, control_name="Empty_Test", error_message="Empty", reverse="F"):
        control_empty = sp.Simple_control(control_name,  column_name, error_message, self.datasource, showed,reverse)
        control_empty.boolean_control = pd.isna(self.datasource[column_name]) # Check empty cells and update bool_result list
        self.update_DataFrame(control_empty)

    def Isequal(self, column_name,showed,control_name="Equality_Test", error_message="wrong value",reverse="F",*values):
        control_isequal= sp.Simple_control(control_name,  column_name, error_message, self.datasource, showed,reverse)
        control_isequal.boolean_control = self.datasource[column_name].apply(lambda x : True if x in values else False)
        self.update_DataFrame(control_isequal)

    def update_DataFrame(self, control):

        if not isinstance(control, sp.Simple_control) and not isinstance(control, cp.Complex_control): #Load bool result in the DataFrame
            raise TypeError("control must be a Simple_control or a Complex_control")

        if control.control_name not in self.bool_result.columns:
            self.bool_result.insert(0, str(control.control_name), "")

        for i, cel in enumerate(control.boolean_control):
            if control.reverse == "F":
                self.bool_result.at[i, control.control_name] = cel
            if control.reverse == "T":
                if cel is False:
                    self.bool_result.at[i, control.control_name] = True
                if cel is True:
                    self.bool_result.at[i, control.control_name] = False

        if control.showed == 1:     #Load text result in the DataFrame
            if control.control_name not in self.text_result.columns:
                self.text_result.insert(0, str(control.control_name), "")
                control.build_text_result()

            for i, cel in enumerate(control.commented_anomaly):
                self.text_result.at[i, control.control_name] = cel

    def list_columns(self):
        print(self.bool_result.columns)

    def complex_control(self,control_name, error_message, control_validation,showed):
        comp_c = cp.Complex_control(control_name, error_message, self.bool_result,control_validation,showed)
        self.update_DataFrame(comp_c)

montest = Control_center(r'D:\Users\sgasmi\Desktop\Source.xlsx', 'source')

#montest = Control_center(r'C:\Users\Sabri.GASMI\Desktop\Jeu - Copie.xlsx', 'Feuil1')
t1 = time.clock()


montest.empty("Nom", 1, "Nom", "haa","T")
montest.empty("Prénom", 1, "Prénom", "fgg")
montest.empty("Prénom", 1, "Prénom non vide", "Non vide","T")
montest.Isequal("Prénom",1, "Test_prenom", "Non vide","T","Alain","Robert","Thierry")
montest.empty("Prénom", 1,"BLALAL","T")
#test = cp.Complex_control("TestC","Erreur",montest.bool_result,"Nom*Prénom",0)
"""
montest.empty("Date de naissance", 1, "Date naiss", "Date naissance vide")
montest.empty("Clé situation de famille", 1, "Ctr Clé situation de famille", "Situation vide",)
montest.first_raws("Matricule", "Nom")
"""
t2 = time.clock()
print(montest.bool_result)
print(t2 - t1)

"""
cols = df.columns.tolist()
>>> cols = [cols[-1]]+cols[:-1] # or whatever change you need
>>> df.reindex(columns=cols)"""