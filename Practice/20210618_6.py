'''
Count Inversions
https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1#

'''

class Solution:
    # User function Template for python3
    # arr[]: Input Array
    # N : Size of the Array arr[]
    # Function to count inversions in the array
    def merge(self,arr,aux,l,mid,r):

        i = k = l
        j = mid + 1
        inv = 0
        while i <= mid and j <= r:
            if arr[i] > arr[j]:
                aux[k] = arr[j]
                inv += (mid - i + 1)  # number of inversions for all elements right side of a[i]
                j += 1
                k += 1
            else:
                aux[k] = arr[i]
                i += 1
                k += 1
        #copying remaining elements in left part
        while i <= mid:
            aux[k] = arr[i]
            i += 1
            k += 1
        #copying remaining elements in right part
        while j <= r:
            aux[k] = arr[j]
            j += 1
            k += 1
        for i in range(l, r + 1, 1):
            arr[i] = aux[i]
        return inv

    def mergesort(self, arr, aux, l, r):
        inv=0
        if l<r:
            mid = (l + r) // 2
            print(l, mid, r)
            inv += self.mergesort(arr, aux, l, mid)
            inv += self.mergesort(arr, aux, mid + 1, r)
            inv += self.merge(arr,aux,l,mid,r)
        return inv


    def inversionCount(self, arr, n):
        inv = 0
        aux = [0]*n
        return self.mergesort(arr, aux, 0, n - 1)

obj=Solution()
arr=[7,6,5,4,3,2,1]
print(obj.inversionCount(arr,len(arr)))