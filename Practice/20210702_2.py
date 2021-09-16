'''
Longest Palindrome in a String
https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1#
'''


class Solution:
    def longestPalin(self, S):
        n = len(S)
        if not S:
            return -1
        if n == 1:
            return S
        S = list(S)
        maxlen = 0
        start = end = -1
        '''
        create all possible even and odd palindromes
        '''
        for i in range(1, n):
            length = 1
            low = i - 1
            high = i + 1
            while low >= 0 and high < n and S[low] == S[high]:
                length += 2
                low -= 1
                high += 1
            if length > maxlen:
                start = low + 1
                end = high - 1
                maxlen = length
            low = i - 1
            high = i
            length = 0
            while low >= 0 and high < n and S[low] == S[high]:
                length += 2
                low -= 1
                high += 1
            if length > maxlen:
                start = low + 1
                end = high - 1
                maxlen = length
        print(maxlen)
        # print(start,end)
        if maxlen == 0 or maxlen == 1:
            return "".join(S[0])
        result = "".join(S[start:end + 1])
        return result
obj = Solution()
# S="abc"
#S="aaaabbaa"
S = "rfkqyuqfjkxy"
print(obj.longestPalin(S))
