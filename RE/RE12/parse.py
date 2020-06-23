def hasNum(instr):
    return any(c.isdigit() for c in instr)

def parse(filename):
    with open(filename, 'r') as f:
        c = f.readlines()
        c = [s.strip() for s in c]
        for i in range(len(c)):
            if hasNum(c[i]) or c[i] == ")":
                c[i] += ","
        s = "".join(c)
        s = "(" + s + ")"
        return eval(s)

def main():
    print(parse("tuple1.txt"))

if __name__ == "__main__":
    main()