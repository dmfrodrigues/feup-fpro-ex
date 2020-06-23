import functools as ft

def map_reduce(n1,n2):
    l = [x*x for x in range(n1,n2+1) if x%2 == 1]
    ret = ft.reduce(lambda x,y: x*y if x*y<50 else x+y, l)
    return ret

print(map_reduce(0, 10))
print(map_reduce(5, 100))
