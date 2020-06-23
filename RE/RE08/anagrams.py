def mycomp(s):
    return s.lower()

def mycomp_diff(t):
    ret = []
    for s in t:
        ret += (s.lower(),)
    return ret

def getletters(s):
    s = s.lower()
    s = ''.join(sorted(s))
    s = s.replace(' ', '')
    return s

def anagrams(alist):
    tpllist = []
    for s in alist:
        tpllist.append((getletters(s), s))

    tpllist = sorted(tpllist)

    if len(tpllist) == 0:
        return []

    ret = [[tpllist[0][1]]]
    
    for i in range(1, len(tpllist)):
        t = tpllist[i]
        t_ = tpllist[i-1]
        if t[0] == t_[0]:
            ret[len(ret)-1].append(t[1])
        else:
            ret.append([t[1]])

    for t in ret:
        t = sorted(t, key=mycomp)
    ret = sorted(ret, key = mycomp_diff)
    
    return ret

print(anagrams(["they see", "eat", "The eyes", "car has", "ate", "a crash", "tea"]))
print(anagrams(["sentence", "lives", "ten scene", "bat", "Elvis", "CE sennet"]))
print(anagrams([]))


