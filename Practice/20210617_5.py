'''
 Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/
'''
from collections import defaultdict


def findDuplicate(nums):
    dic = defaultdict(list)#creating a dictionary that stores list values
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    print(dic)
    for key, value in dic.items():
        if value > 1:
            return key

nums=[1,3,4,2,2]
#nums=[1,1]
print(findDuplicate(nums))