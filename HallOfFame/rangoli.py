def rangoli(N):
    m = ["" for i in range(2*N-1)]
    for i in range(N):
        m[i] += "--"*(N-1-i)
        for c in range(N-1, N-i-2, -1):
            m[i] += chr(ord('a')+c)+"-"
        m[i] = m[i][:2*N-1]
        m[i] = m[i][0:2*N-2]+m[i][::-1]
    for i in range(N, 2*N-1):
        m[i] = m[2*N-i-2]
    ret = m[0]
    for i in range(1, 2*N-1):
        ret += "\n"+m[i]
    return ret

print(rangoli(1))
print(rangoli(3))
#print(rangoli(12))

