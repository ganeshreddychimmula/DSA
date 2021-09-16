'''
    array[] = [3,4,5,6,7,8,9,10,1,2]
    
    condition : array is rotated but sorted in ascending order

    We rotate an ascending order sorted array at some point unknown to user. So for instance,
    3 4 5 6 7 might become 5 6 7 3 4. Modify binary search algorithm to find an element in the rotated array in O(log n) time
    and O(1) Space complexity
    directly searching for target element without searching for pivot element first
'''


def binarysearch(array, s):
    low = 0
    high = len(array) - 1

    while low <= high:
        # print(low,high)
        mid = (low + high) // 2
        if array[mid] == s:
            return mid
        if array[mid] > array[low]:  # if true means left of mid is strictly increasing
            if array[mid] > s and array[low] <= s:  # if true means target is on left strictly increasing prt of mid
                high = mid - 1
            else:  # means target is on right but graph is strictly increasing on left part of mid
                low = mid + 1
        else:  # means right of mid is strictly increasing
            if array[mid] < s and array[high] >= s:  # if true means target is on right strictly increasing part of mid
                low = mid + 1
            else:  # means target is on left but graph is strictly increasing on right part of mid
                high = mid - 1
    else:
        return "not found"


arr = [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
s = int(input())
print(binarysearch(arr, s))
