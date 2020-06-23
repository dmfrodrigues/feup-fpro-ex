def transpose(m):
    return [[m[j][i] for i in range(len(m[0]))] for j in range(len(m))]

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

def is_identity(m):
    N = len(m)
    I = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        I[i][i] = 1
    return (m == I)

def is_orthogonal(mx):
    mt = transpose(mx)
    product = mult(mx,mt)
    return is_identity(product)

print(is_orthogonal([[-1, 0], [0,1]]))
print(is_orthogonal([[-2,3], [4,-1]]))