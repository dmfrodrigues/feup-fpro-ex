def wc(filename):
    with open(filename) as f:
        c = f.readlines()
        ret = [0,0,0]
        for s in c:
            ret[0] += 1
            ret[1] += len(s.split())
            ret[2] += len(s)
        return tuple(ret)

print(wc("shakespeare.txt"))
print(wc("monty.txt"))
