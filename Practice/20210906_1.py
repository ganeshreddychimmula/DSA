'''
Algorithimic toolbox
week four
programming assignment
program 1 - Binary search

'''


def binarysearch(arr, n, k):
    l = 0
    h = n-1
    while l<=h:
        mid = l + (h-l)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            h = mid - 1
        else:
            l = mid + 1
    return -1
'''
inp1 = list(map(int, input().strip().split()))
n = inp1[0]
arr1 = inp1[1:]
inp2 = list(map(int, input().strip().split()))
k = inp2[0]
arr2 = inp2[1:]
'''
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
5 1 5 8 12 13
5 8 1 23 1 11
Output:
2 0 -1 0 -1
'''
'''
5
1 5 8 12 13
5
8 1 23 1 11
Output:
2 0 -1 0 -1
'''
