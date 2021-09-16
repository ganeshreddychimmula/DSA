'''
LB’s list- Smallest subarray with sum greater than x
https://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1#
'''
class Solution:
    def sb(self, a, n, x):
        sm=0
        min_len=10000
        i=j=0
        while j<n :
            #print(i,j,sm)
            while sm<=x and j<n:
                sm+=a[j]
                j+=1
            while sm>x and i<=j:
                if j-i <min_len:
                    min_len=j-i
                sm-=a[i]
                i+=1
        return min_len

obj=Solution()
arr=[1, 4, 45, 6, 0, 19]#result=10
print(obj.sb(arr,len(arr),51))