P = float(input("Principal amount: "))
r = float(input("Interest rate (%): "))/100
n = float(input("Frequency of payment per year: "))
t=2.0
A = P*(1+r/n)**(n*t)
print("Money:", A)