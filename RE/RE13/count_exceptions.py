def count_exceptions(f, n1, n2):
    ret = 0
    for i in range(n1, n2+1):
        try:
            f(i)
        except:
            ret += 1
    return ret

print(count_exceptions(lambda x: 1/(abs(x)-2), -5, 5))
print(count_exceptions(lambda x: 1/0 if x > 10 else 0, 0, 50))