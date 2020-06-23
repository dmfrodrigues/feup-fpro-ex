def cut(filename, delimiter, field):
    if type(field) != list: field = [field]
    field = [x-1 for x in field]
    with open(filename, 'r') as f:
        c = f.readlines()
        ret = ""
        for s_ in c:
            s = s_.strip().split(delimiter)
            ret += s[field[0]]
            for d in field[1:]:
                ret += delimiter + s[d]
            ret += "\n"
        return ret[:-1]

def main():
    print(repr(cut("data.csv", ",", 2)))
    print(repr(cut("data.csv", ",", [2,4])))

    
