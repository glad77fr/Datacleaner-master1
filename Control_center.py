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
        except:
            print("the excel file doest exist")

    def empty(self, column_name, showed, control_name="Empty_Test", error_message="Empty"):
        control_empty = sp.Simple_control(control_name, column_name, error_message, self.datasource, showed)
        control_empty.bool_result = pd.isna(self.datasource[column_name]) # Check empty cells and update bool_result list
        control_empty.build_text_result()
        print(control_empty.text_result)


montest = Control_center(r'D:\Users\sgasmi\Desktop\source.xlsx', 'source')

montest.empty("Nom", 1, "Vide", "haa")