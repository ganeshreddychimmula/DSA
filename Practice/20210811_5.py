'''
nmodm effircent algorithm
'''
# we need to find fib(n)%m, but, this is time conduming for largee numbers
# so we need to find the repeating sequence for n%m
# we know repeating sequence of fib(n)%m starts with 01
def fibonacci(n, m):
    if n<=1:
        return n
    else:
        a = 0 # current -2
        b = 1 # current term -1
        fib = 1
        for i in range(1,n):
            fib = a+b
            if fib % m == 1 and b % m == 0: # checking for  01 sequence
                # i is length of repeating sequence
                # fib(n) % m == fib(n%i) % m
                return fibonacci(n % i, m)
            a = b
            b = fib
        return fib%m


n, m = map(int, input().strip().split())
print(fibonacci(n, m))
'''
2015 3
1
239 1000
161
2816213588 239
151
'''