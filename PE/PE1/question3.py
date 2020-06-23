num = float(input("num:"))
x = num-1
x_ = -2
while abs(x - x_) > 0.000001:
    x_ = x
    x = (x+num/x)/2
print("%.3f"%x)
