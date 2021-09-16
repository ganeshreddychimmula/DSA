'''
Union and Intersection of two sorted arrays
https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1#
Given two arrays a[] and b[] of size n and n respectively. The task is to find union between these two arrays.

Union of the two arrays can be defined as the set containing distinct elements from both the arrays.
If there are repetitions, then only one occurrence of element should be printed in union.
'''
def doUnion( a, n, b, m):
    i = 0
    j = 0
    count = 0
    arr = set()#we considered set becuase we only set only takes unique values
    loop = True

    while i < n and j < m:#if both haven't reached end then put the smallest into
        if a[i] == b[j]:
            arr.add(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            arr.add(b[j])
            j += 1
        else:
            arr.add(a[i])
            i += 1
        continue
    while i < n and j == m:
        arr.add(a[i])
        i += 1
        continue
    while j < m and i == n:
        arr.add(b[j])
        j += 1
        continue
    #print(arr,i,m)
    return len(arr)

a=[1,2,3,4,5]
n=len(a)
b=[1,2,3,3,6,7,8,9,10,99]
m=len(b)
print(doUnion(a,n,b,m))
