'''
Longest consecutive subsequence
https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1#
'''


class Solution:
    # arr[] : the input array
    # N : size of the array arr[]

    # Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self, arr, n):
        s = set()
        max_count = 0
        # set doesn't take duplicates
        for ele in arr:
            s.add(ele)
        # check each possible element from start
        # check if element is 1st in consequtive sequence
        for i in range(n):
            count = 1  # considering first element
            if arr[i] - 1 not in s:
                j = arr[i]
                while j in s:
                    j += 1
                # j-arr[i] gives length of sequence
                max_count = max(max_count, j - arr[i])
        return max_count

obj=Solution()
arr=[2,6,1,9,4,5,3]
arr=[1,9,3,10,4,20,2]
print(obj.findLongestConseqSubseq(arr,len(arr)))