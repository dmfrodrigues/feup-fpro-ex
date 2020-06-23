def diff(filename1, filename2):
    with open(filename1) as f1:
        c1 = f1.readlines()
        with open(filename2) as f2:
            ret = ""
            c2 = f2.readlines()
            curr2 = 0
            for i in range(len(c1)):
                b = -1
                for j in range(curr2, len(c2)):
                    if c1[i] == c2[j]:
                        b = j
                        break
                if b == -1:
                    ret += "- %s\n"%c1[i].strip()
                else:
                    for k in range(curr2, b):
                        ret += "+ %s\n"%c2[k].strip()
                    curr2 = b+1
            for i in range(curr2, len(c2)):
                ret += "+ %s\n"%c2[i].strip()
            return ret

print(diff("file1d.txt", "file2d.txt"))