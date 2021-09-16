'''
Array Subset of another array
https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1#
'''
from collections import defaultdict


def isSubset(a1, a2, n, m):
    if m > n:
        return "No"
    d = defaultdict(int)
    # if we do it with array then searching an element each time is tedious
    for i in a1:
        d[i] = 1
    j = 0
    while j < m:
        if d[a2[j]] != 1:
            return "No"
        j += 1

    return "Yes"
arr1=[11, 1, 13, 21, 3, 7]
arr2=[11, 3, 7, 1]


print(isSubset(arr1,arr2,len(arr1),len(arr2)))