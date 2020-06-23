d   = int(input("d="))
num = int(input("num="))
n = num
ans = 0
while n != 0:
    tmp = n%10 
    if(tmp > d):
        ans += 2*tmp
    n //= 10
print(ans)
