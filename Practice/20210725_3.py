'''
https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
'''


def search( arr, target):
    if len(arr) == 1:
        return 0
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        # condition where mid is target
        if arr[mid] == target:
            return mid
        # when mid is on left strictly increasing curve
        if arr[mid] >= arr[low]:
            # target is on left increasing side
            if arr[mid] > target and arr[low] <= target:
                high = mid - 1
            # target is on right not strictly increasing side
            else:
                low = mid + 1
        # when mid is on right strictly increasing side
        else:
            # target is on right side
            if arr[mid] < target and arr[high] >= target:
                low = mid + 1
            # target is on left of mid
            else:
                high = mid - 1
    return -1
arr=[4,5,6,7,0,1,2]
arr1=[3,1]
print(search(arr1,1))