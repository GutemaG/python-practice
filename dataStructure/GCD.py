def gcd(m,n):
    while(n%m!=0):
        r=n%m
        n=m
        m=r
    return m

print(gcd(48,36))
print(gcd(434,966))
