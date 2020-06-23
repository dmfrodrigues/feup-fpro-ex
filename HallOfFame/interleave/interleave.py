def interleave(f1, f2):
    s = ""
    with open(f1) as instrm1:
        content1 = instrm1.readlines()
        print(content1)
        with open(f2) as instrm2:
            content2 = instrm2.readlines()
            print(content2)
            for i in range(min(len(content1), len(content2))):
                if i < len(content1):
                    s += content1[i]
                if i < len(content2):
                    s += content2[i]
    return s

print(interleave("monty.txt", "shakespeare.txt"))