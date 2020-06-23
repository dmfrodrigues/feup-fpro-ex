def solver(a,b,c):
    d = b*b - 4*a*c
    if a != 0:
        if d < 0:
            return list()
        elif d == 0:
            return [-b/(2*a)]
        else:
            d = d**0.5
            s1 = (-b+d)/(2*a)
            s2 = (-b-d)/(2*a)

            if s1 < s2:
                return [s1, s2]
            else:
                return [s2, s1]
    else:
        return [-c/b]


print(solver(10,2,1))
print(solver(1,2,1))
print(solver(1,3,2))
print(solver(-1,3,2))
print(solver(1,2,0))
print(solver(-1,2,0))
print(solver(2,5,-3))