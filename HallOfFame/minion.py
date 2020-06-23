def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

def mycmp(t):
    return (len(t[0]), t[0], t[1])

def minion(astring):
    astring = astring.upper()
    N = len(astring)
    s = []
    for sz in range(1,N+1):
        for l in range(0, N-sz+1):
            if not(astring[l:l+sz] in s):
                s.append(astring[l:l+sz])
    #s_ = list(s)
    #s_.sort()
    #print(s_)

    kevin = 0
    kevin_lst = []
    stuart = 0
    stuart_lst = []
    for subs in s:
        n = occurrences(astring, subs)
        if subs[0] == "A" or \
           subs[0] == "E" or \
           subs[0] == "I" or \
           subs[0] == "O" or \
           subs[0] == "U":
            kevin += n
            kevin_lst.append((subs, n))
        elif ord('A') <= ord(subs[0]) and ord(subs[0]) <= ord('Z'):
            stuart += n
            stuart_lst.append((subs, n))
        
    #kevin_lst.sort(key=mycmp)
    #stuart_lst.sort(key=mycmp)

    ret = ""
    
    if kevin > stuart:
        ret = "The winner was Kevin with a total of %d points:"%kevin
        for i in kevin_lst:
            ret += "\n- %s: %d"%(i[0], i[1])
    elif kevin == stuart:
        ret = "It was a draw!"
    else:
        ret = "The winner was Stuart with a total of %d points:"%stuart
        for i in stuart_lst:
            ret += "\n- %s: %d"%(i[0], i[1])

    return ret

#print(minion("ANANAS"))
print(minion("BANANA"))
#print(minion("U"))
#print(minion("Z"))
#print(minion(""))
#print(minion("AABZABZAB"))

