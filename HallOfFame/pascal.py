"""
Write a Python function pascal(n) that, for a given integer n, returns a string with the first n rows of the Pascal's triangle.
Each row finishes by "\n" (newline) and each value is separated by a single space. The value at the n-th row and r-th column of
the triangle is equal to n!/(r!*(n-r)!).
    for the number n=3, the result is the string 1\n1 1\n1 2 1
    for the number n=5, the result is the string 1\n1 1\n1 2 1\n1 3 3 1\n1 4 6 4 1
"""
def pascal(n):
    m = [[0 for i in range(n+1)] for j in range(n+1)]
    for l in range(n):
        m[l][0] = 1
        for c in range(1, l+1):
            m[l][c] = m[l-1][c-1] + m[l-1][c]
    s = ""
    for l in range(n):
        for c in range(0,l):
            s += str(m[l][c]) + " "
        s += str(m[l][l])
        if l != n-1:
            s += "\n"
    
    return s

print(repr(pascal(3)))
print(repr(pascal(5)))