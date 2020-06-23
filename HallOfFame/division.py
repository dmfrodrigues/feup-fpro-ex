def division(a,b):
    try:
        r = a/b
    except ZeroDivisionError:
        return "can't divide by 0!"
    except TypeError:
        return "unsupported operand type(s) for division"
    return str(a) + "/" + str(b) + " = " + str(r)
print(division(10,2))
print(division(10,0))
print(division(10,'b'))
