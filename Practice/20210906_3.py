'''
Algorithimic toolbox
week four
programming assignment
program 3 - majority number suing divide and conquer
'''
def count(arr, k, l, h):
    cnt=0
    for i in range(l, h+1, 1):
        if arr[i]==k:
            cnt+=1
    return cnt
def mergesort(arr, l, h):
    if l<=h:
        if l == h:
           return arr[l]
        mid = l + (h-l)//2
        e1 = mergesort(arr, l, mid)
        e2 = mergesort(arr, mid+1, h)
        if e1 == e2:
            return e1
        else :
            ele = e1 if count(arr, e1, l, mid)>count(arr, e2, mid+1, h) else e2
            return ele

def majority(arr, n):
    ele= mergesort(arr, 0, n-1)
    cnt = count(arr, ele, 0, n-1)
    if cnt > n//2:
        return 1
    else:
        return 0

n = int(input())
arr = list(map(int, input().strip().split()))
print(majority(arr, n))
'''
Input:
5
2 3 9 2 2
Output:
1
2 is the majority element.
10
512766168 717383758 5 126144732 5 573799007 5 5 5 405079772
output:
0
'''