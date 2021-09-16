'''
greedy algorithms coursera assignment 3
'''

def minrefills(stops, D, maxd, n):
    refill = 0
    current = 0
    limit = maxd
    i = 0
    while True:
        if limit >= D:
            return refill
        if i>=n or (i<n and stops[i] > limit):
            return -1
        # reach farthest stop possible under current limit
        while i<n and stops[i] <= limit:
            i+=1
        limit = stops[i-1] + maxd
        refill += 1


D = int(input())
maxd = int(input())
n = int(input())
stops = list(map(int, input().strip().split()))
print(minrefills(stops, D, maxd, n))
'''
950
400
4
200 375 550 750
Output:
2

10
3
4
1 2 5 9
Output:
-1

200
250
2
100 150
output:
0
'''