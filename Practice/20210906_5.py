'''
Algorithimic toolbox
week four
programming assignment
program 5 - Inversions
'''
# we use mergesort to find out no. of inversions
def merge(arr, l, mid, h):
    dup = arr[:] # duplicate array
    k = l
    i = l
    j = mid+1
    inv = 0
    while i <= mid and j <= h:
        # compare ith and jth element and put smallest element into dup array
        if arr[i] <= arr[j]:
            dup[k] = arr[i]
            i += 1
            k += 1
        else:
            inv += mid - i + 1
            dup[k] = arr[j]
            j += 1
            k += 1
    while i <= mid:
        dup[k] = arr[i]
        i += 1
        k += 1
    while j <= h:
        dup[k] = arr[j]
        j += 1
        k += 1
    for i in range(l, h+1, 1):
        arr[i] = dup[i]
    # print(arr)
    return inv


def inversions(arr, l, h):
    inv = 0
    if l<h:
        mid = l + (h-l)//2
        # division of array about mid
        inv += inversions(arr, l, mid)
        inv += inversions(arr, mid+1, h)
        # merge operation merges sub arrays
        inv += merge(arr, l, mid, h)
    return inv



n = int(input())
arr = list(map(int, input().strip().split()))
print(inversions(arr, 0, n-1))

'''
5
2 3 9 2 9
Output:
2
'''