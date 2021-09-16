'''
https://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/
Given an array of n distinct integers sorted in ascending order,
write a function that returns a Fixed Point in the array,
if there is any Fixed Point present in array, else returns -1.
Fixed Point in an array is an index i such that arr[i] is equal to i.
Note that integers in array can be negative.
'''


# problem states that it has distinct integers so we just need to find sub-sequence where condition meets
def valueEqualToIndex(arr, n):
    # code here
    low = 0
    high = n - 1
    start = end = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == mid+1 and (mid == 0 or arr[mid-1] != mid):
            start = mid
            break
        elif arr[mid] >= mid+1:
            high = mid-1
        else:
            low = mid+1
    low=start
    high=n-1
    while low <= high:
        mid = (low+high)//2
        print(mid)
        if arr[mid] == mid+1 and (mid == n-1 or arr[mid+1] != mid+2):
            end = mid
            break
        elif arr[mid] <= mid+1:
            low = mid+1
        else:
            high = mid-1
    print(start,end)
    return arr[start : end + 1]

arr1 = [-10, -5, 3, 4, 7, 9]
arr = [-10, -5, 3, 4, 5, 6, 7, 8, 9]
arr=[1,33]
print(valueEqualToIndex(arr, len(arr)))
