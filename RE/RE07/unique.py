def unique(atuple):
    atuple = sorted(atuple)
    ret = ()
    ret += (atuple[0],)
    for i in range(1, len(atuple)):
        if atuple[i] != atuple[i-1]:
            ret += (atuple[i],)
    return ret

print(unique((8,8,1,3,1,3,5)))
print(unique((1,1,1,1)))
