def hash(num):
    sum = 0
    for s in str(num):
        sum += int(s)
    return sum%8

def collisions(alist):
    ret = dict()
    for n in alist:
        h = hash(n)
        if h in ret:
            ret[h] += 1
        else:
            ret[h] = 1
    return ret

print(collisions([24, 42]))
print(collisions([1, 789, 100, 9807, 1208, 92, 101]))
