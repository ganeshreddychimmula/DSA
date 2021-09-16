'''
38. Count and Say
https://leetcode.com/problems/count-and-say/submissions/
'''
import itertools
class Solution:
    def countAndSay(self, n):
        result="1"
        for _ in range(n-1):
            v="" # accumulator string
            # iterate the characters grouped(digits) by digit
            for digit,group in itertools.groupby(result):
                count = len(list(group))
                v += "%i%s"%(count,digit)
            result = v
        return result

obj=Solution()
print(obj.countAndSay(9))