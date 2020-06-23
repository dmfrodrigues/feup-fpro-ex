def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

def minion_game(astring):
    N = len(astring)
    m = {}
    for l in range(0,N):
        for r in range(l+1, N+1):
            s = astring[l:r]
            if s in m.keys():
                m[s] += 1
            else:
                m[s] = 1

    kevin = 0
    stuart = 0
    for subs in m.keys():
        if subs[0] == "A" or \
           subs[0] == "E" or \
           subs[0] == "I" or \
           subs[0] == "O" or \
           subs[0] == "U":
            kevin += m[subs]
        else:
            stuart += m[subs]
        
    if kevin > stuart:
        ret = "Kevin %d"%kevin
    elif kevin == stuart:
        ret = "Draw"
    else:
        ret = "Stuart %d"%stuart

    print(ret)

if __name__ == '__main__':
    s = input()
    minion_game(s)

