'''
Merge two sorted arrays with O(1) extra space
approach1
https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays5135/1#

'''
def merge(ar1,ar2,n,m):
    #we traverse each element from end of ar2
    #print(ar1,ar2)
    for i in range(m-1,-1,-1):
        #traversing through ar1 for smallest element greater than ar2[j]
        #move all elements one step ahead till smallest greater element is found
        #to creaet space for the ar2[i] in ar1 in it's rightfull position
        #as for the last element store it tempororily
        last=ar1[n-1]
        #print(last)
        j=n-2
        while j>=0 and ar1[j]>ar2[i]:
            ar1[j+1]=ar1[j]
            j-=1
        #checking if there is a need to put ar2[i] in ar1
        if (j!=n-2 or last > ar2[i]):
            ar1[j+1]=ar2[i]
            ar2[i]=last
            print(i,j+1,ar1,ar2)






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