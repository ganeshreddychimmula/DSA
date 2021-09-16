'''
Row with max 1s
https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1#
'''
import sys


class Solution:

    def rowWithMax1s(self, arr, n, m):
        count = 0
        mx = -1
        index = -1
        row = sys.maxsize
        for i in range(n):
            j = m - 1
            count = 0
            while j >= 0 and arr[i][j] == 1:
                count += 1
                j -= 1
            # print(count)
            if count > mx and count > 0:
                mx = count
                index = i
        return index

obj=Solution()
arr=[[0, 1, 1, 1],
           [0, 0, 1, 1],
           [1, 1, 1, 1],
           [0, 0, 0, 0]]
print(obj.rowWithMax1s(arr,len(arr),len(arr[0])))
