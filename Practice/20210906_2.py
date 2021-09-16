'''
Algorithimic toolbox
week four
programming assignment
program 2 - Binary search with duplicates
'''
def binarysearch(arr, n, k):
    l = 0
    h = n-1
    while l<=h:
        mid = l + (h-l)//2
        if arr[mid] == k and (mid == 0 or arr[mid-1]!=k):
            return mid
        elif arr[mid] >= k:
            h = mid-1
        else:
            l = mid + 1
    return -1

n = int(input())
inp1 = list(map(int, input().strip().split()))
k = int(input())
inp2 = list(map(int, input().strip().split()))
# print(arr1, arr2)
# print(binarysearch(arr1, n, 8))
for i in range(k):
    if i == k-1:
        print(binarysearch(inp1, n, inp2[i]))
    else:
        print(binarysearch(inp1, n, inp2[i]),end=" ")
'''
sample input:
Input:
7
1 5 8 8 12 12 13
5
8 1 23 1 12
Output:
2 0 -1 0 4
'''