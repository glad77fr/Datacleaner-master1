import pandas as pd
import itertools
import re

class Complex_control():

    def __init__(self, control_name, error_message, source,control_validation,showed):
        self.control_name = control_name  # name of control
        self.error_message = error_message  # error message of control
        self.source = source  # source of control
        self.control_validation = control_validation # text that detail the logic control
        self.showed = showed  # Booleean control, if 0 then the anomaly will be invisible, if 1 it will be visible
        self.boolean_control = []  # List where boolean results of anomaly control will be stored
        self.boolean_truth =[] # List of boolean value that are accepted as true
        self.list_control = []
        self.__control_attr()
        self.__bool_transformation()
        self.__build_list_control()
        self.__list_intermediate = [] # List the booleans values of the control
        self.__build___list_intermediate()



    def __control_attr(self):
        if not isinstance(self.control_name, str):  # control if control_name is a string
            raise TypeError("control_name must be set to a string")

        if not isinstance(self.error_message, str):  # control if error_message is a string
            print(self.error_message)
            raise TypeError("error_message must be set to a string")

        if not isinstance(self.source, pd.DataFrame):  # source if error_message is a DataFrame
            raise TypeError("source must be set to a DataFrame")

        if not isinstance(self.showed, int):  # control if showed is an integer
            raise TypeError("showed must be set to an integer")

        if not isinstance(self.error_message, str):  # control if error_message is a string
            print(self.error_message)
            raise TypeError("error_message must be set to a string")

    def __bin_count_or(self,val):
        # Transformation into table of truth for or values
        bin_list = list(itertools.product([0, 1], repeat=val * 2))
        bin_list2 = []
        res_list = []

        for el in bin_list:
            bin_list2.append(list(el))

        for el in bin_list2:
            if str(el).count("1") >= 1:
                res_list.append(el)

        return res_list

    def __bin_count_xor(self, val):
        # Transformation into table of truth for xor values
        bin_list = list(itertools.product([0, 1], repeat=val * 2))
        bin_list2 = []
        res_list = []

        for el in bin_list:
            bin_list2.append(list(el))

        for el in bin_list2:
            if str(el).count("1") == 1:
                res_list.append(el)

        return res_list

    def __ins(self, list1, list2):
        # fusion of the two list
        res = []
        if any(isinstance(el, list) for el in list1) and any(isinstance(el, list) for el in list2):
            for i, el in enumerate(list1):
                for j, val in enumerate(list2):
                    res.append(el + val)
        return res

    def __bool_transformation(self):
        list_validation = []
        control_validation = self.control_validation
        bool_validation = ""
        code_validation= ""
        prev_val = ""

        for val in control_validation: #step one: extraction of special characters
            if val in ["*", "-", "~"]:
                bool_validation = bool_validation + val
        if bool_validation == "":
            raise TypeError("control_validation must contain at least a special character: * - ~")

        cpt = 0

        for i in range(0, len(bool_validation), 1): #step two: transform bool_validation into a synthetic expression save in code_validation

            if bool_validation[i] == "*":
                if prev_val == "-":
                    code_validation = code_validation + "O" + str(cpt)
                    cpt = 0
                if prev_val == "~":
                    code_validation = code_validation + "X" + str(cpt)
                    cpt = 0
                cpt += 1
                prev_val = "*"

            if bool_validation[i] == "-":
                if prev_val == "~":
                    code_validation = code_validation + "X" + str(cpt)
                    cpt = 0
                if prev_val == "*":
                    prev_val = code_validation + "E" + str(cpt)
                prev_val = "-"
                cpt += 1

            if i == len(bool_validation) - 1 and prev_val == "-":
                code_validation = code_validation + "O" + str(cpt)

            if bool_validation[i] == "~":
                if prev_val == "-":
                    code_validation = code_validation + "O" + str(cpt)
                    cpt = 0
                if prev_val == "*":
                    prev_val = code_validation + "E" + str(cpt)

                prev_val = "~"
                cpt += 1

            if i == len(bool_validation) - 1 and prev_val == "~":
                code_validation = code_validation + "X" + str(cpt)

            if i == len(bool_validation) - 1 and prev_val == "*":
                code_validation = code_validation + "E" + str(cpt)

        for i, val in enumerate(code_validation): #Transform code validation into boolean validation
            if val == "E":
                if list_validation:
                    l = []
                    j = []
                    for n in range(int(code_validation[i + 1])):
                        l.append(1)
                    j.append(l)
                    list_validation = self.__ins(list_validation, j)
                else:
                    l = [1]
                    for n in range(int(code_validation[1])):
                        l.append(1)
                    list_validation.append(l)

            if val == "O":
                if list_validation:
                    list_validation = self.__ins(list_validation, self.__bin_count_or(int(code_validation[i + 1])))
                else:
                    for j, val in enumerate(self.__bin_count_or(int(code_validation[i + 1]))):
                        list_validation.append(val)
            if val == "X":
                if list_validation:
                    list_validation = self.__ins(list_validation, self.__bin_count_xor(int(code_validation[i + 1])))
                else:
                    for j, val in enumerate(self.__bin_count_xor(int(code_validation[i + 1]))):
                        list_validation.append(val)
        print(list_validation, "liste 1")

    def __build_list_control(self):
        control_validation = self.control_validation
        self.list_control=re.split('[-*~]', control_validation)

    def __build___list_intermediate(self):
        nb = 1
        for i, val in enumerate (self.list_control):
            res=[]

            for val in list(self.source[val].tolist()):
                res.append(val)


            if not self.__list_intermediate:

                for val in res:
                    self.__list_intermediate.append(val)
            else:
                if nb == 1:
                    nb = 2
                    self.__list_intermediate = [[i,j] for i, j in zip(self.__list_intermediate,res)]
                    print("ok",nb)
                else:
                    for i, val in enumerate(range(len(self.__list_intermediate))):
                        self.__list_intermediate[i].append(res[i])



        print(self.__list_intermediate)








data_source = pd.DataFrame()

#a = Complex_control("Complexe","flflf",data_source,"dldl*jjj",1)
