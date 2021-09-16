'''
Key Pair
https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/
only works if array has positive numbers only
'''
from collections import defaultdict


# User function Template for python3
class Solution:
    def hasArrayTwoCandidates(self, arr, n, x):
        rem = [0] * x

        for i in range(n):
            # because we only have positive integers and if arr[i] >x then pass
            if arr[i] < x:
                rem[arr[i] % x] += 1
            for i in range(1, x // 2, 1):
                if rem[i] >= 1 and rem[x - i] >= 1:
                    return True
            # for middle element
            # if even middle element should repeat 2 times
            if x % 2 == 0:
                if rem[x // 2] > 1:
                    return True
            else:  # x is odd
                if rem[x // 2] > 0 and rem[x - x // 2] > 0:
                    return True
        return False

obj=Solution()
arr=[3,3,5,0,0,3,1,4]
arr=[1,4,45,6,10,8]
print(obj.hasArrayTwoCandidates(arr,len(arr),16))