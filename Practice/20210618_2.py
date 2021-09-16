'''
Merge two sorted arrays with O(1) extra space
approach4
https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays5135/1#
gap method
'''
def nextgap(gap):
    if gap<=1:
        return 0
    return (gap//2)+gap%2#for odd numbers floor of n/2 + 1 else n/2
def merge(ar1,ar2,n,m):
    gap=n+m#wholelength
    gap=nextgap(gap)
    while gap>0:
        #comparing elements in ar1
        i=0
        while i+gap<n:
            if ar1[i]>ar1[i+gap]:
                ar1[i],ar1[i+gap]=ar1[i+gap],ar1[i]
            i+=1

        #comapring elements from both arrays
        j=0#normal case if gap <n and i+gap start from j=0
        if gap>n:#that if gap greater than len of ar1 we can choose j as gap-n
            j=gap-n
        while i<n and j<m:
            if ar1[i]>ar2[j]:
                ar1[i],ar2[j]=ar2[j],ar1[i]
            i+=1
            j+=1

        #comparing elements from arr2
        j=0
        while j+gap<m:
            if ar2[j]>ar2[j+gap]:
                ar2[j], ar2[j + gap] = ar2[j + gap], ar2[j]
            j+=1

        #print(ar1,ar2)

        gap=nextgap(gap)







ar1 = [1, 5, 9, 10, 15, 20]
ar2 = [2, 3, 8, 13]
n = len(ar1)
m = len(ar2)

merge(ar1, ar2, n, m)

print("After Merging \nFirst Array:", end="")
for i in range(n):
    print(ar1[i], " ", end="")

print("\nSecond Array: ", end="")
for i in range(m):
    print(ar2[i], " ", end="")