import math
def solution(a, b):
    if math.gcd(a,b) != 1:
        a, b = a//math.gcd(a,b), b//math.gcd(a,b)
    f = factorization(b)
    while 2 in f:
        f.remove(2)
    while 5 in f:
        f.remove(5)
    if f == []:
        return 1
    else:
        return 2

            
            
            
def factorization(n):
    factors = []
    i = 2
    while i<=n:
        if n%i == 0:
            factors.append(i)
            n = n/i
        else:
            i = i+1
    return factors