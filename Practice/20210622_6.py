'''
LB’s list- Minimum swaps and K together
https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together4847/1#

'''
def minSwap(arr, n, k) :
    min_swap=999
    nltk=0
    for i in range(n):
        if arr[i]<=k:
            nltk+=1

    for i in range(n-nltk+1):
        l=0
        for j in range(i,i+nltk):
            if arr[j]>k:
                l+=1
        if l<min_swap:
            min_swap=l
    return min_swap
#arr=[4 ,11 ,6 ,5 ,11 ,20 ,19 ,14 ,14 ,2 ,9 ,20 ,11, 11 ,15, 1 ,7 ,12 ,19 ,9]
#print(minSwap(arr,len(arr),14))
arr=[19, 9]
print(minSwap(arr,2,18))