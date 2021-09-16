'''
Subarray with 0 sum
https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1#
Given an array of positive and negative numbers.
Find if there is a subarray (of size at-least one) with 0 sum.
'''
from collections import defaultdict
class Solution:
    # Function to check whether there is a subarray present with 0-sum or not.
    # idea is that if sum of subarray is zero then sum of elements after
    # and beore subarray are equal
    # if a sum repeats then return True
    def subArrayExists(self, arr, n):
        sum_dic = defaultdict(int)
        sm = 0
        for i in range(n):
            sm += arr[i]
            # if that sum is alrady present
            if sum_dic[sm] == 1 or sm == 0:
                return True
            sum_dic[sm] = 1
        return False

        ##Your code here
arr=[9, 4, -2, -1, 5, 0, -5, -3, 2]
obj=Solution()
arr=[1,2,3,4,5]
arr=[4 ,2 ,-3 ,1 ,6]
print(obj.subArrayExists(arr,len(arr)))
