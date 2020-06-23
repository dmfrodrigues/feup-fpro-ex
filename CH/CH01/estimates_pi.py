#Diogo Miguel Ferreira Rodrigues
#up201806429
#1MIEIC05
#2018-Oct-01

import random
import math
import statistics

N = int(input("Number of needles per estimate: "))
needles_inside = 0
needles_outside = 0
pi = [None]*100
for i in range(0,100):
    for j in range(1,N+1):
        x = random.random()
        y = random.random()
        if math.sqrt(x*x+y*y) < 1:
            needles_inside = needles_inside + 1
        else:
            needles_outside = needles_outside + 1

    pi[i] = 4*needles_inside/(needles_inside + needles_outside)
    err = (pi[i] - math.pi)/math.pi
    print("Estimate #", i+1 , ": pi=", pi[i], " (err=", 100*err, "%)")
    
print()
print("pi=(", sum(pi)/100, "+-", statistics.stdev(pi), ")")