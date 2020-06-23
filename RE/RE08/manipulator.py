def manipulator(l, cmds):
    result = ""
    for c in cmds:
        s = c.split()
        if s[0] == "insert":
            l.insert(int(s[1]), int(s[2]))
        elif s[0] == "print":
            result += str(l) + " "
        elif s[0] == "remove":
            l.remove(int(s[1]))
        elif s[0] == "append":
            l.append(int(s[1]))
        elif s[0] == "sort":
            l.sort()
        elif s[0] == "pop":
            l.pop()
        elif s[0] == "reverse":
            l.reverse()
    return result

print(manipulator([], ["insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6", "append 9", "append 1", "sort", "print", "pop", "reverse", "print"]))
print(manipulator([2, 4], ["print", "remove 4", "append 1", "sort", "print", "pop", "reverse", "print"]))
print(manipulator([], ["print"]))
