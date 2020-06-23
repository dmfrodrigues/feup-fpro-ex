def sort_by_field(filename, field):
    with open(filename) as f:
        c = f.readlines()
        names = (c[0].strip()).split(',')
        idx = names.index(field)
        ret = c[0].strip() + "\n"
        c = [(s.strip().split(',')[idx], s.strip()) for s in c[1:]]
        c = sorted(c)
        for s in c:
            ret += s[1] + "\n"
        return ret[:-1]

def main():
    print(sort_by_field("emails.txt", "surname"))
    #print(sort_by_field("emails.txt", "mail"))

if __name__ == "__main__":
    main()

