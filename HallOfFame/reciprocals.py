def reciprocals(alist):
    r = []
    for i in alist:
        try:
            r.append(1/i)
        except:
            pass
    return r
print(reciprocals([4, 2, 8, 1]))
print(reciprocals([0, 4, 2, 'X']))
