from collections import defaultdict


class Solution:

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        n = len(val)
        V = 0
        d = defaultdict(float)
        for i in range(n):
            # key:value => value per weight : index of item
            d[val[i] / wt[i]] = i
        # print(d[0.25])
        keys = list(d.keys())
        # print(keys)
        keys = sorted(keys)
        for i in range(n - 1, 0, -1):
            # print(d[keys[i]],end=" ")
            index = d[keys[i]]
            print(index)
            if wt[index] <= W and W > 0:
                V += val[index]
                W -= wt[index]
        # print(val)
        return V


n = int(input())
W = int(input())
val = list(map(int,input().strip().split()))
wt = list(map(int,input().strip().split()))
ob=Solution()
print(ob.knapSack(W,wt,val,n))
'''
3
50
60 100 120
10 20 30
'''