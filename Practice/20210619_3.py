'''
Rearrange array in alternating positive & negative items with O(1) extra space
https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/
rearrange array positively and negatively without changing
'''
#bad slution Time limited exceeded
class Solution:
    def rearrange(self,arr, n):
        i=j=0#not set
        pos=0
        neg=1
        result=[]
        while i < n and j<n:
            if pos==0 :
                if arr[i]>=0:
                    result.append(arr[i])
                    pos=1
                    i+=1#j not set
                    neg=0
                else:
                    i+=1
            if neg==0:
                if arr[j]<0:
                    result.append(arr[j])
                    neg=1
                    j+=1
                    pos=0
                else:
                    j+=1
        while i<n:
            if arr[i]>=0:
                result.append(arr[i])
                i+=1
        while j<n:
            if arr[j]<0:
                result.append(arr[j])
                j+=1
        for i in range(n):
            arr[i]=result[i]

arr=[9, 4, -2, -1, 5, 0, -5, -3, 2]
obj=Solution()
obj.rearrange(arr,len(arr))
print(arr)
