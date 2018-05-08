import operator
import itertools
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

def bool_result(test):
       #Extraction des signes
       signe = []
       for char in test:
              print(char)
              if char in ["*","-"]:
                     signe.append(char)

       print(signe)
bool_result(test)

malist=list(itertools.product([0,1], repeat=4))

for el in malist:
       for e in el:
              print(e)