

def formal(name):
    name = name.split(" ")
    ret = name[len(name)-1] + ","
    for s in name[:len(name)-1]:
        ret += " "+s[0]+"."
    return ret

#name = input("name:")
#print(formal(name))
