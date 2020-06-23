num = int(input("num="))
total = 0
for i in range(1, num+1):
    if num%i == 0:
        total += i
print(total)
