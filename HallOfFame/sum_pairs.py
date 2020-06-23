def sum_pairs(alist):
    r = []
    for i in range(len(alist)-1):
        try:
            r.append(alist[i] + alist[i+1])
        except:
            pass
    return r
print(sum_pairs([10, 3, 5, 6, 9, 3]))
print(sum_pairs([10, 3, 5, 'NA', 9, 1]))
