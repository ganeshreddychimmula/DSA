'''
Three way partitioning
https://practice.geeksforgeeks.org/problems/three-way-partitioning/1#
'''
class Solution:
    #Function to partition the array around the range such
    #that array is divided into three parts.
    def threeWayPartition(self, array, a, b):
        i=-1
        n=len(array)
        j=n
        k=0
        #doesn't keep array sorted
        while k<j:
            print(k,array)
            if array[k]>=a and array[k]<=b:
                k+=1
            elif array[k]<a  :
                i+=1
                array[i],array[k]=array[k],array[i]
                k+=1
            else:
                j-=1
                array[j],array[k]=array[k],array[j]
        return array
obj=Solution()
arr=[1, 2, 3, 3, 4]
print(obj.threeWayPartition(arr,1,2))