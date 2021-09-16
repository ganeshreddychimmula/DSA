'''
 Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/
'''


def findDuplicate(nums):
    #print(nums)
    ln = len(nums)
    # given that there are range of elements is only 1,ln-1
    #adding ln to every index which is encountered
    for i in range(ln):
        original = nums[i] % ln
        nums[original] += ln
    for i in range(1,ln ):
        if (nums[i] // ln) > 1:
            return i

nums=[1,3,4,2,2]
#nums=[1,1]
print(findDuplicate(nums))