'''
Algorithimic toolbox
week four
programming assignment
program 4 - Improving quicksort
Quick sort with randomised pivot with 3 way partitioning
'''
import random
# partition function uses last element as pivot
# and divides array into 3 parts
# 0 to i has elements < pivot, i+1 to j-1 == pivot, j to h elements greater than pivot
def partition(arr, l, h):
    pivotindex = random.randrange(l, h)# choosing random index for pivot
    arr[h], arr[pivotindex] = arr[pivotindex], arr[h] # swapping pivot element with last element in array
    pivot = arr[h]
    current = l
    j = h
    i = l-1
    while current < j:
        if arr[current] == pivot:
            current += 1
        elif arr[current] < pivot:
            i+=1
            arr[i], arr[current] = arr[current], arr[i]
            current += 1
        else:
            j-=1
            arr[j], arr[current] = arr[current], arr[j]
    arr[h], arr[j] = arr[j], arr[h] #swapping current which is at j+1 position and h
    return i, j+1

def quicksort(arr, l, h):
    if l<h:
        # pivot
        left, right = partition(arr, l, h)
        # applying quicksort on both sub-arrays around i - j part
        quicksort(arr, l, left)
        quicksort(arr, right, h)

n = int(input())
arr = list(map(int, input().strip().split()))
quicksort(arr, 0, n-1)
str=' '.join(map(str,arr))
print(str)

'''
Input:
5
2 3 9 2 2
Output:
2 2 2 3 9

8
6 6 2 7 9 1 1 1 
output:
1 1 1 2 6 6 7 9
'''