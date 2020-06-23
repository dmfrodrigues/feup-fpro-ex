def override(l1,l2):
    inret = []
    ret = []
    for i in l2:
        ret.append(i)
        inret.append(i[0])
    for i in l1:
        if i[0] not in inret:
            ret.append(i)
    ret = sorted(ret)
    return ret

print(override([('c','d'),('c','e'),('a','b'),('a', 'd')],[('a','c'),('b','d')]))
print(override([('a','b','c','e'),('f', 'p', 'r', 'o')], [('a','c'),('b','d')]))
print(override([('a','b'),('c','d')], [('b','a'),('d','c')]))