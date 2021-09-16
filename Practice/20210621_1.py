'''
Count More than n/k Occurences
https://practice.geeksforgeeks.org/problems/count-element-occurences/1#

'''
from collections import defaultdict


class Solution:

    # Function to find all elements in array that appear more than n/k times.
    def countOccurence(self, arr, n, k):
        d = defaultdict(int)
        result = set()
        for i in arr:
            d[i] += 1
            if d[i] > n / k:
                result.add(i)
        return len(result)
obj=Solution()
arr=[2,6,1,9,4,5,3]
arr=[3,1,2,2,1,2,3,3]
print(obj.countOccurence(arr,len(arr),4))