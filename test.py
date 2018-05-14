import operator
import itertools
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

"""

test ="A*B-C"


def bin_res(valeur):
    # Extraction des signes
    signe = []
    for i in valeur:
        if i in ["*", "-","~"]:
            signe.append(i)
    return signe


def bin_count_or(val):

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

print(g)
res=[[1,0,1],[1,1,0]]

def ins(list1,list2):
    res=[]
    if any(isinstance(el, list) for el in list1) and any(isinstance(el, list) for el in list2):
        for i, el in enumerate(list1):
           for j, val in enumerate(list2):
               res.append(el+val)
    return res



#g[1].insert(1,res[0])

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
            resultat = resultat + '*'
            prev_val="*"

        if text[i] == "-":
            if prev_val == "~":
                resultat = resultat + "X" + str(cpt)
                cpt = 0
            prev_val="-"
            cpt +=1

        if i == len(text)-1 and prev_val == "-":
            resultat = resultat + "O" + str(cpt)

        if text[i] =="~":
            if prev_val =="-":
                resultat = resultat + "O" + str(cpt)
                cpt = 0
            prev_val = "~"
            cpt +=1


        if i == len(text)-1 and prev_val == "~":
            resultat = resultat + "X" + str(cpt)




convert_str("j*t-h-l-k~-k**---*~~--~~~~")

j=[[0, 0, 0, 0, 0, 0, 0, 1],[0, 0, 0, 0, 0, 0, 0, 2]]
l=[[1]]
k=ins(l,j)
f=ins([[0],[1]],k)


print(k)
print(f)