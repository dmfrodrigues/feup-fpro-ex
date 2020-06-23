def mult():
    N = 12
    pad = 4
    print(" "*(pad+1), end = '')
    for c in range(1, N+1):
        print(str(c).rjust(pad, " "), end = '')
    print()
    print(" "*(pad), ":", "-"*pad*N, sep = '')
    for l in range(1, N+1):
        print(str(l).rjust(pad, " "), ":", sep = '', end = '')
        for c in range(1, N+1):
            print(str(l*c).rjust(pad, " "), end = '')
        print()
    
mult()