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

    def empty(self, column_name, showed, control_name="Empty_Test", error_message="Empty"):
        control_empty = sp.Simple_control(control_name,  column_name, error_message, self.datasource, showed)
        control_empty.boolean_control = pd.isna(self.datasource[column_name]) # Check empty cells and update bool_result list

        self.update_DataFrame(control_empty)

    def nonempty(self, column_name, showed, control_name="Nonempty_Test", error_message="Nonempty"):
        control_nonempty= sp.Simple_control(control_name, column_name, error_message, self.datasource, showed)
        control_nonempty.boolean_control = pd.notnull(self.datasource[column_name])

        self.update_DataFrame(control_nonempty)

    def update_DataFrame(self, control):

        if not isinstance(control, sp.Simple_control): #Load bool result in the DataFrame
            raise TypeError("control must be a Simple_control")

        if control.control_name not in self.bool_result.columns:

            self.bool_result.insert(0, str(control.control_name), "")

        for i, cel in enumerate(control.boolean_control):

            self.bool_result.at[i, control.control_name] = cel

        if control.showed == 1:     #Load text result in the DataFrame
            if control.control_name not in self.text_result.columns:
                self.text_result.insert(0, str(control.control_name), "")
                control.build_text_result()

            for i, cel in enumerate(control.commented_anomaly):
                self.text_result.at[i, control.control_name] = cel

    def list_columns(self):
        print(self.bool_result.columns)

#montest = Control_center(r'D:\Users\sgasmi\Desktop\Source.xlsx', 'source')

montest = Control_center(r'C:\Users\Sabri.GASMI\Desktop\Jeu - Copie.xlsx', 'Feuil1')
t1 = time.clock()



montest.empty("Nom", 1, "Nom", "haa")
montest.empty("Prénom", 1, "Prénom", "fgg")
montest.nonempty("Nom",1,"gg", "Non vide")
test = cp.Complex_control("TestC","Erreur",montest.bool_result,"Nom-Prénom",0)
"""
montest.empty("Date de naissance", 1, "Date naiss", "Date naissance vide")
montest.empty("Clé situation de famille", 1, "Ctr Clé situation de famille", "Situation vide")
montest.first_raws("Matricule", "Nom")
"""
t2 = time.clock()

print(t2 - t1)
#print(montest.text_result)
"""
cols = df.columns.tolist()
>>> cols = [cols[-1]]+cols[:-1] # or whatever change you need
>>> df.reindex(columns=cols)"""