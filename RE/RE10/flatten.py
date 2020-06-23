def flatten(alist):
    if type(alist) != list:
        return [alist]
    ret = []
    for i in alist:
        ret = ret + flatten(i)
    return ret

print(flatten(['Hello', [2, [[], False]], [True]]))
print(flatten([[]]))
