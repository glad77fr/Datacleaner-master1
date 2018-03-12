import pandas as pd
import Simple_control as sp


class Control_center:
    def __init__(self, path_datasource):
        self.path_datasource = path_datasource  # containing the path of the datasource
        self.__load_excel_datasource()  # transfer of the excel file containing data to source DataFrame
        self.datasource = pd.DataFrame()    #DataFrame containing the analysed dataset

    def __load_excel_datasource(self):
        try:
            self.Excel = pd.ExcelFile(self.path_datasource)
            self.datasource = self.Excel
        except:
            print("the excel file doest exist")


montest = Control_center(r'C:\Users\Sabri\Desktop\Test.xlsx')
