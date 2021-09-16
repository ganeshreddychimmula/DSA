'''
Rearrange array in alternating positive & negative items with O(1) extra space
https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/
rearrange array positively and negatively without changing
'''
class Solution:
    def rearrange(self,arr, n):
        #not set
        neg=[]
        pos=[]
        # copying all positive elements into pos and negative elements in neg
        for i in range(n):
            if arr[i]>=0:
                pos.append(arr[i])
            else:
                neg.append(arr[i])
        #print(pos,neg)
        i=j=k=0
        # copying elements alternatively from pos and neg into  array
        while i<len(pos) and j<len(neg):
            arr[k]=pos[i]
            i+=1
            k+=1
            arr[k]=neg[j]
            j+=1
            k+=1
        while i<len(pos):
            arr[k]=pos[i]
            i+=1
            k+=1
        while j<len(neg):
            arr[k]=neg[j]
            j+=1
            k+=1

arr=[9, 4, -2, -1, 5, 0, -5, -3, 2]
obj=Solution()
obj.rearrange(arr,len(arr))
print(arr)
