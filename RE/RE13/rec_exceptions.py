def rec_exceptions(l):
    ret = []
    for f in l:
        try:
            r = f()
        except Exception as e:
            ret.append(e)
        else:
            ret += rec_exceptions(r)
    return ret
print(rec_exceptions([lambda: 1/0]))
print(rec_exceptions([lambda: [lambda: [1,2,3].index(-1), lambda: ''[2]], lambda: [1,2,3][4], lambda: [lambda: [lambda: 1/0]]]))