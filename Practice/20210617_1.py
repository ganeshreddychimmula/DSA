'''
Kadane's Algorithm
https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1#
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
'''


def maxSubArraySum( a, size):
    max_so_far = current_max = 0
    for i in range(size):
        current_max += a[i]
        if current_max < 0:
            current_max = 0
        if current_max > max_so_far:
            max_so_far = current_max
    return max_so_far

array=[1,2,3,-2,5]
#array=[-1,-2,-3,-4]
print(maxSubArraySum(array,len(array)))