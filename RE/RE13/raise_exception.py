def raise_exception(alist, value):
    ret = []
    for i in alist:
        if i <= value:
            ret.append(ValueError("%d is not greater than %d"%(i, value)))
    return ret
print(raise_exception([1, -2, 3, 0], 3))
print(raise_exception([3], 2))
