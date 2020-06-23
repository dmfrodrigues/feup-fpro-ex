def permuta(alist, step=0):
    ret = []
    if len(alist) == 1:
        return [alist]
    for i in range(len(alist)):
        l = permuta(alist[:i]+alist[i+1:])
        for j in l:
            ret.append([alist[i]]+j)
    return ret

print(permuta(['Joe', 'Mary', 'John']))
print(permuta(['A','B','C']))
