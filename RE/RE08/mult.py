def mult(M,N):
    if(len(M[0]) != len(N)):
        return []
    L = len(M)
    C = len(N[0])
    ret = [[0 for c in range(C)] for l in range(L)]
    for c in range(C):
        for l in range(L):
            for n in range(len(N)):
                ret[l][c] += M[l][n]*N[n][c]
    return ret

print(mult([[1, 2], [3, 4]], [[2, 0], [1, 2]]))
print(mult([[1, 2, 3], [4, 5, 6]], [[9], [8], [7]]))
print(mult([[7, 8, 9, 10]], [[5], [3], [2], [7]]))
print(mult([[7, 8, 9, 10]], [[5], [3], [2]]))
