'''
Longest consecutive subsequence
https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1#
'''
from collections import defaultdict


class Solution:
    # arr[] : the input array
    # N : size of the array arr[]

    # Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, n):
        d = defaultdict(int)
        count = defaultdict(int)
        max_len = 0
        # value represent position in consecutive order
        # for every element at start we give length 1
        for i in range(n):
            d[arr[i]] = 1
        for i in range(n):
            count = 1
            temp = arr[i]
            if d[temp-1]==0:
                while d[temp + 1] == 1:
                    count += 1
                    temp += 1
            # print(arr[i],end,)
                if count > max_len:
                    max_len = count
        return max_len
obj=Solution()
arr=[2,6,1,9,4,5,3]
arr=[1,9,3,10,4,20,2]
print(obj.findLongestConseqSubseq(arr,len(arr)))