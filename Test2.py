import re

def extraction (value):
    values = []
    values = re.split('[-*)~(]',value)
    result = []

    for val in values:
        if val != "" :
            result.append(val)
    return result


def extract_spe(value):
    bool_validation = ""
    for val in value:  # step one: extraction of special characters
        if val in ["*", "-", "~","(",")"]:
            bool_validation = bool_validation + val
    if bool_validation == "":
        raise TypeError("control_validation must contain at least a special character: * - ~")
    return bool_validation


def add_parenthesis(value):
    preval = ""
    ind = 0
    max = len(value) - 1
    count_p = 0
    ind2 = 0

    for i,val in enumerate(value):
        if i == 0 and val == "*":
            value = "(" + value
            ind +=1
            try:
                if value[ind+1] not in ["*",")"]:
                    value = value[:ind + 1] + ")" + value[ind + 1:]
                    ind += 1
            except:
                value = value[:ind + 1] + ")" + value[ind + 1:]
                ind += 1
        else:

            if val == "*" and preval not in ["(","*"]:
                value = value[:ind] + "(" + value[ind:]
                ind += 1

            if val == "*" and i!= max:

                if value[ind+1] not in ["*",")"]:
                    value = value[:ind+1] + ")" + value[ind+1:]
                    ind +=1

            if val == "*" and i == max:
                value = value[:ind + 1] + ")" + value[ind + 1:]
        preval = val
        ind += 1
    ind = 0
    max = len(value) - 1

    for i, val in enumerate(value):
        if val == "(" :
            for y,val in enumerate(value[ind2:]):
                if val == "(" and y != 0:
                    break
                if val == ")":
                    count_p += 1
                    ind2 += 1
                ind2 += 1
            if count_p >1 :
                for j in range(1,count_p):
                    value = value[:ind] + "(" + value[ind:]
                    ind += 1
                    print(ind,"f")
            count_p = 0
        ind += 1

    ind = 0
    ind2 = 0
    for i, val in enumerate(value):
        if val == ")" :
            for y,val in enumerate(value[ind2:]):

                if val == ")" and y != 0:
                    break
                if val == "(":
                    count_p += 1
                    ind2 += 1
                ind2 += 1
            if count_p >1 :
                for j in range(1,count_p):
                    value = value[:ind] + ")" + value[ind:]
                    ind += 1
                    print(ind,"f")
            count_p = 0
        ind += 1

    return value

def add_values(values,expression):
    ind_exp = 0
    ind_val = 0
    newexpression =""
    for i,val in enumerate(expression):
        ind_exp +=1

        if val =="*":
            if newexpression != "":
                newexpression = newexpression[:ind_exp-1] + values[ind_val] + newexpression[ind_exp-1:]
                ind_exp +=   len(values[ind_val])
                ind_val += 1
            else:
                newexpression = expression[:ind_exp-1] + values[ind_val] + expression[ind_exp-1:]
                ind_exp += len(values[ind_val])
                ind_val += 1

        if val == ")" and expression[i-1] == "*":
            newexpression = newexpression[:ind_exp-1] + values[ind_val] + newexpression[ind_exp-1:]
            ind_exp += len(values[ind_val])
            ind_val += 1

        if val in ["-", "~"] and expression[i-1] != ")":
            if newexpression != "":
                   newexpression = newexpression[:ind_exp-1] + values[ind_val] + newexpression[ind_exp-1:]
                   ind_exp += len(values[ind_val])
                   ind_val += 1
            else :
              newexpression = expression[:ind_exp-1] + values[ind_val] + expression[ind_exp-1:]
              ind_exp += len(values[ind_val])
              ind_val += 1

        if val in ["-", "~"] and i == 0:
            newexpression = values[ind_val] + expression[ind_exp-1:]
            ind_exp += len(values[ind_val])
            ind_val += 1

        if val in ["-", "~"]:
            try:
                expression[i+1]
            except:
               newexpression = newexpression[:ind_exp+1] + values[ind_val] + newexpression[ind_exp+1:]
               ind_exp += len(values[ind_val])
               ind_val += 1

    return newexpression

exp = "a*b"
exp2 = "a-b*c"
exp3 = "a*r*e-f"
exp4 = "(a*b)-c"
expression = extract_spe(exp4)
print(expression,"expression")
valeurs = extraction(exp4)
print(valeurs,"valeurs")
parenthesis = add_parenthesis(expression)
print(parenthesis,"parenthesis")

print(add_values(valeurs, parenthesis))



