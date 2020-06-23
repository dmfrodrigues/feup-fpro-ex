def permuta(alist, step=0):
    ret = []
    if step == len(alist)-1:
        return [alist]

    for i in range(step, len(alist)):
        l = alist[:]
        l[step], l[i] = l[i], l[step]
        ret = ret + permuta(l, step+1)
    return ret

print(permuta(['Joe', 'Mary', 'John']))
print(permuta(['A','B','C']))
