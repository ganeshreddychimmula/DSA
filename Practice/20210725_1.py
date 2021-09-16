'''
First and last occurrences of x
https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1#
'''


def find(arr, n, x):
    start = end = -1
    low = 0
    high = n-1
    # less or equal is required because when position at high it is useful
    while low <= high:
        mid = (low + high) // 2
        # to check first occurence of array
        if arr[mid] == x and (mid == 0 or arr[mid - 1] != x):
            start = mid
            break
        # when mid points to element on right of first occurence
        elif arr[mid] >= x:
            high = mid - 1
        # when mid points to element on left of first occurence
        else:
            low = mid + 1
    # low is not changed
    low = start
    high = n-1
    while low <= high:
        mid = (low + high) // 2
        # to check first occurence of array
        if arr[mid] == x and (mid == n - 1 or arr[mid + 1] != x):
            end = mid
            break
        # when mid points to element on left of last occurrence
        elif arr[mid] <= x:
            low = mid + 1
        # when mid points to element on right of last occurrence
        else:
            high = mid - 1

    return start, end

arr=[1, 3, 5, 5, 5, 5, 67, 123, 125]
arr2=[1, 3, 5, 5, 5, 5, 7, 123, 125 ]
arr3=list(map(int,input().strip().split()))
a,b=find(arr3,len(arr3),8)
print(a,b)
# 1 1 1 2 3 3 3 4 4 4 4 4 5 5 6 7 7 7 8 8 8 8 9 9 9 9 9 10 10 10