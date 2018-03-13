import pandas as pd
import Simple_control as sp


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
            self.datasource = self.Excel.parse('data3')

        except:
            print("the excel file doest exist")

    def empty(self, column_name, showed, control_name="Empty_Test", error_message="Empty"):
        control = sp.Simple_control(control_name, column_name, error_message,self.datasource, self.bool_result,self.text_result,showed)

#ef __init__(self, control_name, column_name, error_message, source, bool_result,text_result, showed=0):


#montest = Control_center(r'C:\Users\Sabri\Desktop\Test.xlsx')
montest = Control_center(r'D:\Users\sgasmi\Desktop\data3.xlsx', 'data3')
montest.empty("Nom", 0, "Vide", "haa")