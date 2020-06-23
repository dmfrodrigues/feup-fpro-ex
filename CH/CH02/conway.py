import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import time

def process_neighbours(m, x, y):
    s = 0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            s += m[i][j]
    s -= m[x][y]
    if m[x][y]:
        if s < 2 or s > 3:
            return 0
        else:
            return 1
    else:
        if s == 3:
            return 1
        else:
            return 0

instr = input()
instr = instr.split()
C = int(instr[0])
L = int(instr[1])

curr_matrix = [[0 for x in range(C)] for y in range(L)]
for l in range(L):
    instr = input(); instr = instr.split()
    for c in range(C):
        curr_matrix[l][c] = int(instr[c])

#curr_matrix[3][3] = 1
#curr_matrix[3][4] = 1
#curr_matrix[3][5] = 1

prev_matrix = [[0 for x in range(C)] for y in range(L)]

plt.ion()
fig, ax = plt.subplots()
cmap = ListedColormap(['w', 'k'])
obj = ax.imshow(curr_matrix, cmap=cmap)

while True:
# for _ in range(4):

    #for l in range(L):
    #    print(curr_matrix[l])
    #print()

    plt.show()
    plt.pause(0.01)

    obj.set_data(curr_matrix)

    prev_matrix = curr_matrix
    curr_matrix = [[0 for x in range(C)] for y in range(L)]

    for l in range(1, L-1):
        for c in range(1, C-1):
            curr_matrix[l][c] = process_neighbours(prev_matrix, l, c)
