import operator
import itertools
import re
import pandas as pd
import numpy as np
import numpy



"""
ops = {"+": operator.add,
       "-": operator.sub,
       "*": operator.mul}

op_char = "+"
op_func = ops[op_char]
a=3
b=78
result = op_func(a, b)
print(result)


a=[1,2,3,4,5,6]

b=[7,8,9,10,11,12]

k=[3,3,5]
v=[10,3,5]

y = list(zip(a,b,k,v))
j =[]
for val in y:
    j.append(list(val))

"""


a=[3,4]
b=[1,9]
c=[8,4]

d= {'C1': a,'C2':b,'C3':c}
h = pd.DataFrame(data=d)

print(h)

def fus():
    a=[]
    for i, val in enumerate(h.itertuples()):
        a.append(
            h[])
#y = [[i, j] for i, j in zip(x,k)]
#print(x)



a = [['a'], ['c']]
b = [['d'],  ['e']]
c = list(zip(a,b))
print(c[0])

#print(list(zip(['a', 'b', 'c'], ['d', 'e', 'f'])))
a = True
b = True
c = False
print (a and b or c, "cool")

a = [[False,False],[False,False]]
b = [[1,1]]
for i,val in enumerate(a):
    if a[i] in b:
        print("ok")

a="bal*dfs*f-k*fk ht"
g =re.split('[-*]',a)
print(g)


test ="A*B-C"


def bin_res(valeur):
    # Extraction des signes
    signe = []
    for i in valeur:
        if i in ["*", "-","~"]:
            signe.append(i)
    return signe


def bin_count_or(val):
 #Transformation into table of truth for or values
    bin_list = list(itertools.product([0,1], repeat=val*2))
    bin_list2=[]
    res_list = []

    for el in bin_list:
        bin_list2.append(list(el))

    for el in bin_list2:
        if str(el).count("1") >= 1:
            res_list.append(el)

    return res_list

def bin_count_xor(val):
    # Transformation into table of truth for xor values
    bin_list = list(itertools.product([0,1], repeat=val*2))
    bin_list2=[]
    res_list = []

    for el in bin_list:
        bin_list2.append(list(el))

    for el in bin_list2:
        if str(el).count("1") == 1:
            res_list.append(el)

    return res_list

g=bin_count_xor(1)


res=[[1,0,1],[1,1,0]]

def ins(list1,list2):
    #fusion of the two list
    res=[]
    if any(isinstance(el, list) for el in list1) and any(isinstance(el, list) for el in list2):
        for i, el in enumerate(list1):
           for j, val in enumerate(list2):
               res.append(el+val)
    return res

a =[[1,1,1]]
b =[[0, 1], [1, 0], [1, 1]]
#print(ins(a,b))

def convert_str(val):
    resultat=""
    text=bin_res(val)
    prev_val=""

    cpt = 0

    for i in range(0, len(text), 1):

        if text[i] == "*":
            if prev_val == "-":
                resultat = resultat + "O" + str(cpt)
                cpt = 0
            if prev_val == "~":
                resultat = resultat + "X" + str(cpt)
                cpt=0

            cpt += 1
            prev_val="*"

        if text[i] == "-":
            if prev_val == "~":
                resultat = resultat + "X" + str(cpt)
                cpt = 0
            if prev_val == "*":
                prev_val = resultat + "E" + str(cpt)
            prev_val="-"
            cpt +=1

        if i == len(text)-1 and prev_val == "-":
            resultat = resultat + "O" + str(cpt)

        if text[i] =="~":
            if prev_val =="-":
                resultat = resultat + "O" + str(cpt)
                cpt = 0
            if prev_val == "*":
                prev_val = resultat + "E" + str(cpt)

            prev_val = "~"
            cpt +=1

        if i == len(text)-1 and prev_val == "~":
            resultat = resultat + "X" + str(cpt)

        if i == len(text)-1 and prev_val == "*":
            resultat = resultat + "E" + str(cpt)

    return resultat

convert_str("**")

j=[[0, 0, 0, 0, 0, 0, 0, 1],[0, 0, 0, 0, 0, 0, 0, 2]]
l=[[1]]
k=ins(l,j)
f=ins([[0],[1]],k)

def str_into_bool(str_value):
    result = []

    for i, val in enumerate(str_value):
        if val == "E":
            if result:
                l = []
                j = []
                for n in range(int(str_value[i+1])):
                    l.append(1)
                j.append(l)
                result = ins(result, j)
            else:
                l = []
                for n in range(int(str_value[1])):
                    l.append(1)
                result.append(l)

        if val =="O":
            if result:
                result = ins(result,bin_count_or(int(str_value[i+1])))
            else:
                for j,val in enumerate(bin_count_or(int(str_value[i+ 1]))):
                        result.append(val)
        if val =="X":
            if result:
                result =ins(result,bin_count_xor(int(str_value[i+1])))
            else:
                for j,val in enumerate(bin_count_xor(int(str_value[i+1]))):
                    result.append(val)
    return result


print(str_into_bool("E1X2O1"))