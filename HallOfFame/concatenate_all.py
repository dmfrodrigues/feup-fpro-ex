def concatenate_all(alist):
    #alist = sorted(alist, key = lambda s: s.split("/")[-1])
    ret = ""
    for p in alist:
        try:
            f = open(p, 'r')
            ret += f.read()
            f.close()
        except:
            pass
    return ret

print(repr(concatenate_all(["/usr/", "/usr/share/dict/words", "/root/file.txt"])))
