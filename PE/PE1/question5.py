lower = int(input("lower="))
upper = int(input("upper="))
is_prime = [True]*(upper+1)
is_prime[0] = False
is_prime[1] = False
for i in range(0, len(is_prime)):
    if is_prime[i]:
        for j in range(2*i, len(is_prime), i):
            is_prime[j] = False

print("Prime numbers between", lower, "and", upper, "are:", end=" ")

for i in range(max(lower,0), upper+1):
    if is_prime[i]:
        print(i, end = " ")
print()