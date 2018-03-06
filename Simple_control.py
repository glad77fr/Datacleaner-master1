import pandas as pd

class Simple_control:
    def __init__(self, control_name, column_name, error_message, source, showed):
        self.control_name = control_name #name of control
        self.column_name = column_name #name of column that will be controled
        self.error_message = error_message #error message of control
        self.source = source #source of control
        self.showed = showed # Booleean control, if 0 then the anomalie will be invisible in the rapport, if 1 it will be visible
        self.boolean_control = [] # List where boolean results of anomaly control will be stored
        self.commented_anomaly = [] # liste where commented anomaly will be stored

        if not isinstance(self.control_name,str): # control if control_name is a string
            raise TypeError("control_name must be set to a string")

        if not isinstance(self.column_name, str): # control if column_name is a string
            raise TypeError("column_name must be set to a string")

        if not isinstance(self.error_message, str): # control if error_message is a string
            raise TypeError("error_message must be set to a string")

        if not isinstance(self.source, pd.DataFrame): # source if error_message is a DataFrame
            raise TypeError("source must be set to a DataFrame")

        if not isinstance(self.showed, int): # control if showed is an integer
            raise TypeError("showed must be set to an interger")


    def colonne(self):
        print(self.source.columns)

#    def __set__self.control_name(self, value):
    #    if not isinstance(value, int):
        #    raise TypeError("bar must be set to a string") ggGg

Excel = pd.ExcelFile(r'D:\Users\sgami\Desktop\Test.xlsx')
df = Excel.parse('Test')
test = Simple_control("test","Matricule","Anomalie etrange",df,1)
test.colonne()