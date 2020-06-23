def find(l, c, matrix, word):
    if l < 0 or c < 0 or l > len(matrix) or c > len(matrix[0]):
        return False
    if(len(word) == 0):
        return True
    if(matrix[l][c] != word[0]):
        return False
    w = word[1:]
    return (find(l-1,c-1, matrix, w) or find(l-1,c, matrix, w) or find(l-1,c+1, matrix, w) or \
            find(l  ,c-1, matrix, w) or find(l  ,c, matrix, w) or find(l  ,c+1, matrix, w) or \
            find(l+1,c-1, matrix, w) or find(l+1,c, matrix, w) or find(l+1,c+1, matrix, w))

def soup(matrix, word):
    for l in range(len(matrix)):
        for c in range(len(matrix[0])):
            if find(l, c, matrix, word):
                return (str(chr(l+ord('A'))) + str(c+1))

mx = (('X', 'A', 'B', 'N', 'T', 'O'),\
      ('Y', 'T', 'N', 'R', 'I', 'T'),\
      ('U', 'P', 'O', 'M', 'D', 'S'),\
      ('I', 'O', 'H', 'U', 'O', 'O'),\
      ('R', 'T', 'E', 'L', 'Q', 'X'),\
      ('I', 'W', 'J', 'K', 'P', 'Z'))

print(soup(mx, 'PORTO'))
print(soup(mx, 'HOTEL'))
print(soup(mx, 'RIO'))