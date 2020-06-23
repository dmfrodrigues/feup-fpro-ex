tS = float(input("tS="))
tC = float(input("tC="))
tR = float(input("tR="))
t = tS+tC+tR

tS_lim  = 1.5/2  #0.75
tC_lim  = 40/20  #2
tR_lim  = 10/8   #1.25
t_lim   = 4

if   t  >=  t_lim: 
    print("Time")
elif tS >   tS_lim:
    print("Swimming")
elif tC >   tC_lim:
    print("Cycling")
elif tR >   tR_lim:
    print("Running")
else:
    print(t)
