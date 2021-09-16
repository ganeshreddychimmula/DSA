'''
Chocolate Distribution Problem
https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1#

'''


class Solution:

    def findMinDiff(self, arr, n, m):
        gap = m - 1
        arr.sort()
        min_diff = 999999

        for i in range(n - m + 1):
            # print(arr[i+m-1]-arr[i],arr[i],arr[i+m-1])
            if arr[i + m - 1] - arr[i] < min_diff:
                min_diff = arr[i + m - 1] - arr[i]

        return min_diff
obj=Solution()
arr=[17 ,83 ,59 ,25 ,38 ,63 ,25 ,1 ,37]#result=10
print(obj.findMinDiff(arr,len(arr),9))