import operator

ops = {"+": operator.add,
       "-": operator.sub,
       "*": operator.mul,
       "/": operator.div}

op_char = "+"
op_func = ops[op_char]
a=3
b=78
result = op_func(a, b)