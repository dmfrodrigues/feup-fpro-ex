def fib(n):
    ret = [0]*n
    if n >= 1:
        ret[0] = 0
    if n >= 2:
        ret[1] = 1
    for i in range(2,n):
        ret[i] = ret[i-1] + ret[i-2]
    return ret

print(fib(1))
print(fib(5))