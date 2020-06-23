num = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def rec_to_base(n, base):
    n = int(n)
    base = int(base)
    ret = ""
    while n > 0:
        ret = ret + num[n%base]
        n //= base
    return ret[::-1]

print(rec_to_base(20,16))
print(rec_to_base(20,2))
