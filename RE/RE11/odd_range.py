def odd_range(start, stop, step):
    start = start + (start%2 == 0)
    for i in range(start, stop, 2*step):
        yield i

print(list(odd_range(1, 10, 1)))
print(list(odd_range(100, 150, 5)))
print(list(odd_range(10, 0, 1)))