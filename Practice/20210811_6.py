'''
last digit of fibonacci sum
'''
# find length of repeating sequence
def repeatseqlen():
    j = 0
    sum = 1
    a = 0
    b = 1
    while j>-1:
        fib = (a+b)%10
        sum += fib
        sum %= 10
        # print(sum,end=" ")
        # checking for repeatation of sequence 01
        if sum == 1 and (10+sum-fib)%10 == 0 :
            return j+1 # len
        j+=1
        a = b
        b = fib
        if j==1000:
            return None


def fibonaccisumlastdigit(n):
    if n<=1:
        return n
    else:
        sum = 1
        a = 0
        b = 1
        fib = 1
        for _ in range(1,n):
            fib = (a+b)%10
            sum += fib
            sum %= 10
            # we check if any sum last digit subsequence if sum is repeating
            a = b
            b = fib
        return sum
n = int(input())
len = repeatseqlen()
print(fibonaccisumlastdigit(n%len))
# print(repeatseqlen())
'''
3
4
100
5
832564823476
-
240
0
'''