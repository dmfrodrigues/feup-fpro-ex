def summary_ranges(astr):
    astr = astr.split(",")
    for i in range(len(astr)):
        astr[i] = int(astr[i])
    
    ret = ""
    left = astr[0]    

    for i in range(1, len(astr)):
        if astr[i-1]+1 != astr[i]:
            if left == astr[i-1]:
                ret += str(left) + ","
            else:
                ret += str(left) + "->" + str(astr[i-1]) + ","
            left = astr[i]
    
    if left == astr[-1]:
        ret += str(left)
    else:
        ret += str(left) + "->" + str(astr[-1])
    return ret

print(summary_ranges("0,1,2,3,4,5,7,10,11,20,21"))
print(summary_ranges("1,3,4,6,7,9,10"))
