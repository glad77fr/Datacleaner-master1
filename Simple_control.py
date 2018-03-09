import pandas as pd
import sys as syst


class Simple_control:

    def __init__(self, control_name, column_name, error_message, source, showed, bool_dest, descr_dest):
        self.control_name = control_name  # name of control
        self.column_name = column_name  # name of column that will be controled
        self.error_message = error_message  # error message of control
        self.source = source  # source of control
        self.showed = showed  # Booleean control, if 0 then the anomalie will be invisible in the rapport, if 1 it will be visible
        self.boolean_control = []  # List where boolean results of anomaly control will be stored
        self.commented_anomaly = []  # list where commented anomaly will be stored
        self.bool_dest = bool_dest # DataFrame containing results
        self.descr_dest =descr_dest # DataFrame containing anomalies description

        if not isinstance(self.control_name, str):  # control if control_name is a string
            raise TypeError("control_name must be set to a string")

        if not isinstance(self.column_name, str):  # control if column_name is a string
            raise TypeError("column_name must be set to a string")

        if not isinstance(self.error_message, str):  # control if error_message is a string
            raise TypeError("error_message must be set to a string")

        if not isinstance(self.source, pd.DataFrame):  # source if error_message is a DataFrame
            raise TypeError("source must be set to a DataFrame")

        if not isinstance(self.showed, int):  # control if showed is an integer
            raise TypeError("showed must be set to an integer")

        if not isinstance(self.bool_dest,pd.DataFrame):
            raise TypeError("bool_dest must be set to a DataFrame")

        self.__check_column()   # call check method to searched if column_name exist in the dataframe 'source'

    def __check_column(self):
        """Check if searched column exist"""
        res = False
        for ch in self.source.columns:
            if ch == self.column_name:
                res = True
        if not res:
            print("Erreur, le champs " + self.column_name + " est inexistant dans le fichier")
            syst.exit()

    def colonne(self):
        print(self.source.columns)

    def import_bool (self):


#Excel = pd.ExcelFile(r'D:\Users\sgami\Desktop\Test.xlsx')
#df = Excel.parse('Test')
#test = Simple_control("test", "Matricule", "Anomalie etrange", df, 1)
#test.colonne()
Excel = pd.ExcelFile(r'C:\Users\Sabri.GASMI\Desktop\Jeu.xlsx')
df = Excel.parse('Feuil1')
df_bool = pd.DataFrame()
test = Simple_control("test", "Matricule Groupe", "Anomalie etrange", df, 1, "df_bool")