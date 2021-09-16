'''
LB’s list- Minimum swaps and K together
https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together4847/1#

'''
def minSwap(arr,n,k):
    bad=0
    wsize=0
    for i in range(n):
        if arr[i]<=k:
            wsize+=1
    for i in range(wsize):
        if arr[i]>k:
            bad+=1
    print(wsize,bad)
    if wsize==n:
        return 0
    min_swaps = 999
    left=1
    right=left+wsize-1
    #calculating swaps per each window
    while right<n:
        if arr[left-1]>k:
            bad-=1

        if arr[right]>k:
            bad+=1

        min_swaps=min(bad,min_swaps)
        left+=1
        right+=1

    return min_swaps

arr=[4 ,11 ,6 ,5 ,11 ,20 ,19 ,14 ,14 ,2 ,9 ,20 ,11, 11 ,15, 1 ,7 ,12 ,19 ,9]
print(minSwap(arr,len(arr),14))
#arr=[4, 3 ]
#print(minSwap(arr,2,11))