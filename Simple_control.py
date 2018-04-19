import pandas as pd
import sys as syst


class Simple_control:
    def __init__(self, control_name, column_name, error_message, source, showed=0):
        self.control_name = control_name  # name of control
        self.column_name = column_name  # name of column that will be controled
        self.error_message = error_message  # error message of control
        self.source = source  # source of control
        self.showed = showed  # Booleean control, if 0 then the anomalie will be invisible in the rapport, if 1 it will be visible
        self.boolean_control = []  # List where boolean results of anomaly control will be stored
        self.commented_anomaly = []  # list where commented anomaly will be stored

        if not isinstance(self.control_name, str):  # control if control_name is a string
            raise TypeError("control_name must be set to a string")

        if not isinstance(self.column_name, str):  # control if column_name is a string
            raise TypeError("column_name must be set to a string")

        if not isinstance(self.error_message, str):  # control if error_message is a string
            raise TypeError("error_message must be set to a string")

        if not isinstance(self.source, pd.DataFrame):  # source if error_message is a DataFrame
            raise TypeError("source must be set to a DataFrame")

        if not isinstance(self.showed, int):  # control if showed is an integer
            raise TypeError("showed must be set to an interger")

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

    def build_text_result(self):
        if self.showed == 1:
            self.commented_anomaly = self.boolean_control
            self.commented_anomaly = [self.error_message if x is True else "" for x in self.commented_anomaly]

    def colonne(self):
        print(self.source.columns)




