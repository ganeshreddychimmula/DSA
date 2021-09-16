from math import sqrt
n = int(input())
#n -= 1
Phi = ((1+sqrt(5))/2)**n
phi = ((1-sqrt(5))/2)**n
print(((Phi) - (phi)) / sqrt(5))
