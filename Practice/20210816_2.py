'''
greedy algorithms coursera assignment 2
'''
def maxvalue(vw, W, n):
    V = 0
    vw = sorted(vw)
    # print(vw)
    for i in range(n-1, -1, -1):
        if W>0:
            a = min(W, vw[i][2])
            V += a*(vw[i][1]/vw[i][2])
            W -= a
        else:
            break
    return V

n, W = map(int,input().strip().split())
vw = [[0, 0, 0]]*n
for i in range(n):
    v, w = map(int,input().strip().split())
    vw[i] = [v/w, v, w]
print("%.4f"%maxvalue(vw, W, n))
'''
3 50
60 20
100 50
120 30
Output:
180.0000

1 10
500 30
Output:
166.6667
'''