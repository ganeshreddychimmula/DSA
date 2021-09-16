'''
Trapping Rain Water
https://www.youtube.com/watch?v=m18Hntz4go8
https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1
'''
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        #two pointer approach
        right_max=arr[n-1]
        left_max=arr[0]
        left=0
        right=n-1
        total=0
        while left<=right:
            #if there exists a element on right not less than right
            #then we are sure that water stays there
            if arr[left]<=arr[right]:
                if arr[left]>left_max:
                    left_max=arr[left]
                    left+=1
                else:
                    total+=left_max-arr[left]
                    left+=1
            else:
                if arr[right]>=right_max:
                    right_max=arr[right]
                    right-=1
                else:
                    total+=right_max-arr[right]
                    right-=1
        return total
obj=Solution()
arr=[8 ,8 ,2, 4 ,5 ,5 ,1]#result=10
print(obj.trappingWater(arr,len(arr)))