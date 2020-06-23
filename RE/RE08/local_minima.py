def min_index(alist, l, r):
    ret = 0
    val = int(1e6)
    for i in range(l, r):
        if alist[i] < val:
            val = alist[i]
            ret = i
    return ret

def local_minima(alist, n):
    N = len(alist)
    ret = []
    for i in range(N):
        l = max(0, i-n//2)
        r = min(N, i+n//2+1)
        j = min_index(alist, l, r)
        val = alist[j]
        if alist[j] == alist[i]:
            if len(ret) == 0:
                ret.append((val, j))
                continue

            c = ret[len(ret)-1]
            if not(val == c[0] and j == c[1]):
                ret.append((val, i)) 
    return ret

print(local_minima([10, 3, 3, 14, 5, 7, 4], 3))
print(local_minima([0, 3, 3, 14, 5, 7, 4], 3))
print(local_minima([2, 1, 1, 1, 7, 3, 1], 5))

