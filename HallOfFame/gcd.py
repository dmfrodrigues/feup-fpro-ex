def rec_gcd(m, n):
    if m < n:
        return rec_gcd(n,m)
    else:
        if n == 0:
            return m
        return rec_gcd(n, m%n)

print(rec_gcd(12,14))