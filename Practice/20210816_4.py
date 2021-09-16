'''
greedy algorithms coursera assignment 4
'''
n = int(input())
value = list(map(int, input().strip().split()))
clicks = list(map(int, input().strip().split()))
value = sorted(value)
clicks = sorted(clicks)
res = 0
for i in range(n):
    res += (value[i])*(clicks[i])
print(res)
'''
1
23
39
Output:
897

3
1 3 -5
-2 4 1
Output:
23
23 = 3 · 4 + 1 · 1 + (−5) · (−2).
'''