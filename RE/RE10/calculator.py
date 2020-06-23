def calculator(expr):
    if(type(expr) != tuple):
        return int(expr);
    lhs = calculator(expr[0])
    op = expr[1]
    rhs = calculator(expr[2])
    return eval(str(lhs)+op+str(rhs))

print(calculator((1, '+', 2)))
print(calculator(((1, '+', 2), '*', 3)))
print(calculator(2))
