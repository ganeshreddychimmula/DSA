'''
square root of an integer
https://www.geeksforgeeks.org/square-root-of-an-integer/
'''
def squareroot(n):
    i=1
    while i*i<=n:
        i+=1
    return i-1

print(squareroot(22))