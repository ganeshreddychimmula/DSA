'''
gcd
'''
def gcd(a, b): #lets, use a as dividend, b as divisor and ensure a>b
    if a==b:
        return a
    elif a<b:
        return gcd(b, a)
    else:
        if a%b == 0:
            return b
        else:
            return gcd(b,a%b)
a, b = map(int, input().strip().split())
print(gcd(a,b))
'''
18 35
1
28851538 1183019
17657
'''