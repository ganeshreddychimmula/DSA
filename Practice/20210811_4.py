'''
Lcm of two numbers
'''
# we know that a*b=lcm*gcd
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
def lcm(a,b):
    gcdiv = gcd(a, b)
    lcmul = (a*b)//gcdiv
    return lcmul

a, b = map(int, input().strip().split())
print(lcm(a,b))
'''
6 8
24
761457 614573
467970912861
'''
