'''
Find all pairs of integer array whose sum sum equals given number
https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1#
'''
from collections import defaultdict

#each pair (a,b) repeats two times each time at one elemnt of pair
class Solution:
    def getPairsCount(self, arr, n, k):
        d = defaultdict(int)
        count = 0
        for i in range(n):
            d[arr[i]] += 1

        for i in range(n):
            count += d[k - arr[i]]
            # every time its pair is present it is incremented
            # if a rr[i]=k-arr[i] decrement it's own pair
            if arr[i] == k / 2:
                count -= 1
        return count // 2
arr=[1, 5, 7, 1]
obj=Solution()
print(obj.getPairsCount(arr,len(arr),6))