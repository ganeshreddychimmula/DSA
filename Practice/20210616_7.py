'''

'''
# This function returns k'th smallest element
# in arr[l..r] using QuickSort based method.
# ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT
import sys


def kthSmallest(arr, l, r, k):
    # If k is smaller than number of
    # elements in array
    if (k > 0 and k <= r - l + 1):

        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        pi = partition(arr, l, r)

        # If position is same as k
        if (pi - l == k - 1):#pi-l gives actual position
            return arr[pi]
        if (pi - l > k - 1):  # If position is more,
            # recur for left subarray
            return kthSmallest(arr, l, pi - 1, k)

        # Else recur for right subarray
        return kthSmallest(arr, pi + 1, r , l+(k-1)-pi)#position after pi

    # If k is more than number of
    # elements in array
    return sys.maxsize


# Standard partition process of QuickSort().
# It considers the last element as pivot and
# moves all smaller element to left of it
# and greater elements to right
def partition(arr, l, r):
    pivot = arr[r]
    index = l
    for j in range(l, r):#loops until r-1
        if arr[j] <= pivot:
            arr[index], arr[j] = arr[j], arr[index]
            index += 1
    #putting pivot in it's right position
    arr[index], arr[r] = arr[r], arr[index]
    return index


# Driver Code
if __name__ == "__main__":
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 3;
    print("%d'th smallest element is"%k,
          kthSmallest(arr, 0, n - 1, k))


