import pandas as pd
from xlsxwriter import *


class Toto(Workbook):

    def __del__(self):
        """Close file in destructor if it hasn't been closed explicitly."""
        try:
            if not self.fileclosed:
                self.close()
        except:
            print('lool')
