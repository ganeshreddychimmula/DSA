'''
last number of  alarge fibonacci number
'''
def fibonacci(n):
    if n<=1:
        return n
    else:
        a = 0
        b = 1
        fib = 1
        for _ in range(1,n):
            fib = (a+b)%10
            a = b
            b = fib
        return fib
n = int(input())
print(fibonacci(n))
'''
331
9
'''