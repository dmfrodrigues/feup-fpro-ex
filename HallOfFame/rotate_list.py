def rotate_list(l):
    for i in range(3):
        l.append(l[0])
        del l[0]
    return l

print(rotate_list([1,2,3,4,5,6]))
print(rotate_list([5,20,21,0,-1,3]))
