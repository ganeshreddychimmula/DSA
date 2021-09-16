'''
Trapping Rain Water
https://www.youtube.com/watch?v=m18Hntz4go8
https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1
'''
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        total=0
        largest_right=[0]*n
        largest_left=[0]*n
        left_max=arr[0]
        right_max=arr[n-1]
        for i in range(n):
            if arr[i]>left_max:
                left_max=arr[i]
            largest_left[i]=left_max
        for i in range(n-1,-1,-1):
            if arr[i]>right_max:
                right_max=arr[i]
            largest_right[i]=right_max
        for i in range(n):
            w_height=min(largest_left[i],largest_right[i])
            total+=w_height-arr[i]
        return total

obj=Solution()
arr=[3,0,0,2,0,4]#result=10
print(obj.trappingWater(arr,len(arr)))