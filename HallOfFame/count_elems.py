def count_elems(tup):
    ret = [1]*len(tup)
    for i in range(len(tup)):
        if type(tup[i]) == str or type(tup[i]) == list or type(tup[i]) == tuple:
            ret[i] = len(tup[i])
    return tuple(ret)

print(count_elems((1,'234', 3, 4.0, (5j,))))
print(count_elems(('12',2,(3, 4), [4.0, 'str', 'str2'], 5j)))