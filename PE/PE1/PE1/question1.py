num = int(input("num="))
n = num
ans = 0
while n != 0:
    ans += (n%10)**3
    n //= 10
print(num == ans)
