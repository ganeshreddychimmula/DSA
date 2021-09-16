'''
Given an unsorted array, find the minimum difference between any pair in given array.
Input  : {1, 5, 3, 19, 18, 25};
'''

arr = [1, 19, -4, 31, 38, 25, 100]
arr = sorted(arr)
mn = 99999
for i in range(1,len(arr)):
    mn = min(mn, arr[i]-arr[i-1])

print(mn)