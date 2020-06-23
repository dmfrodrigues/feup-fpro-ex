def isomorphic(astring1, astring2):
    keys = []
    values = []
    for i in range(len(astring1)):
        if astring1[i] not in keys:
            if astring2[i] in values:
                return "'%s' and '%s' are not isomorphic"%(astring1, astring2)
            else:
                keys.append(astring1[i])
                values.append(astring2[i])
        else:
            j = keys.index(astring1[i])
            if values[j] != astring2[i]:
                return "'%s' and '%s' are not isomorphic"%(astring1, astring2)
    for i in range(len(keys)):
        keys[i] = (keys[i], values[i])
    
    ret = "'%s' and '%s' are isomorphic because we can map: "%(astring1, astring2) + str(keys)
    return ret

print(isomorphic('ab', 'aa'))
print(isomorphic('paper', 'title'))
print(isomorphic('foo', 'bar'))
print(isomorphic('turtle', 'tletur'))