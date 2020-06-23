def fetch_middle(lists):
    ret = []
    for l in lists:
        N = len(l)-1
        if N%2 == 0:
            ret.append(l[N//2])
        else:
            ret.append((l[N//2]+l[N//2 + 1])/2)
    return ret

print(fetch_middle([[1,2,3],[4,5,6],[7,8,9,10]]))
print(fetch_middle([[10,25,35,45],[100,-1,3,4],[-3,-5,-10,-20,-100]]))
