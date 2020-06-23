def discard_middle(s):
    N = len(s)
    if N < 4:
        return ""
    return s[:2] + s[-2:]

print(discard_middle("string"))
print(discard_middle("n"))
