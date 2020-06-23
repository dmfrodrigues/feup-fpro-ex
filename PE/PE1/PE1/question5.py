dec = int(input("dec="))
ans = 0
k = 0
while 0 < dec:
    ans += (dec%8)*(10**k)
    k += 1
    dec//=8

print(ans)
