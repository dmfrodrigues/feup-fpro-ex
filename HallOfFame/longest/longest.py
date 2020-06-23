def longest(filename):
    with open(filename) as f:
        cont = f.readlines()
        ret = ""
        for c in cont:
            l = c.replace("\n", " ").split()
            for s in l:
                if len(s) > len(ret):
                    ret = s
        return ret

print(longest("shakespeare.txt"))