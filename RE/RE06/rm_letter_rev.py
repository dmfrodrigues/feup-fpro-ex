

def rm_letter_rev(l, astr):
    i = 0
    while i < len(astr):
        if astr[i] == l:
            astr = astr[:i]+astr[i+1:]
        else:
            i += 1
    return astr[::-1]

#l = input("l:")
#astr = input("astr:")
#print(rm_letter_rev(l, astr))
