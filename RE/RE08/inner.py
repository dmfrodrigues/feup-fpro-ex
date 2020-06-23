def inner(u,v):
    N = len(u)
    ret = 0
    for i in range(N):
        ret += u[i]*v[i]
    return ret

print(inner([], []))
print(inner([1, 2], [2, 4]))
print(inner([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]))
