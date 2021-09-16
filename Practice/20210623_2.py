'''
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/
approach 1
'''
class Solution:
    # mergesort merge operation until (n+m)/2
    def findMedianSortedArrays(self, nums1,nums2):
        i=j=0
        n=len(nums1)
        m=len(nums2)
        mid=(n+m)//2
        aux=[0]*(m+n)
        k=0
        while i<n and j<m and k<mid+1:
            if nums1[i]<nums2[j]:
                aux[k]=nums1[i]
                i+=1
                k+=1
            else:
                aux[k]=nums2[j]
                j+=1
                k+=1
        while i<n and k<mid+1:
            aux[k]=nums1[i]
            k+=1
            i+=1
        while j<m and k<mid+1:
            aux[k]=nums2[j]
            k+=1
            j+=1
        if (m+n)%2==0:
            result = aux[mid-1]+aux[mid]
            return result/2
        else:
            result = aux[mid]
            return result/1
obj=Solution()
arr1=[1,2]
arr2=[3,4]
print(obj.findMedianSortedArrays(arr1,arr2))