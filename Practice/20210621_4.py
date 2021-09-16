'''
Triplet Sum in Array
https://practice.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1#
'''

class Solution:

    # Function to find if there exists a triplet in the
    # array A[] which sums up to X.
    def find3Numbers(self, A, n, k):
        A.sort()
        # we no need to iterate numbers greater than
        for i in range(n - 2):  # O(n*n)
            start = i + 1
            end = n - 1
            rem = k - A[i]
            while start < end:  # O(n)
                if A[start] + A[end] == rem:
                    return True
                elif A[start] + A[end] < rem:
                    start += 1
                else:
                    end -= 1
        return False
obj=Solution()
arr=[3,3,5,0,0,3,1,4]
arr=[1, 4 ,45 ,6 ,10 ,8]
print(obj.find3Numbers(arr,len(arr),13))