def triplet(atuple):
    N = len(atuple)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if atuple[i]+atuple[j]+atuple[k] == 0 and i!=j and i!=k and j!=k:
                    return (atuple[i], atuple[j], atuple[k])
    return ()

print(triplet((-8, 0, 4, -2, -1, 1, 2)))
print(triplet((-1, 1, 1, 1)))
print(triplet((-4, 3, 0, -2, -1, -3)))
