'''
LongestRepeatingSubsequence
https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1#
https://www.geeksforgeeks.org/longest-repeating-subsequence/
'''
class Solution:
    def LongestRepeatingSubsequence(self, s):
        l = len(s)
        L = [[0] * (l + 1) for _ in range(l + 1)]

        for i in range(l + 1):
            for j in range(i,l + 1):
                # because we can ignore s[2][1] if we check s[1][2]
                if i == 0 or j == 0:
                    continue
                elif s[i - 1] == s[j - 1] and i != j:
                    L[i][j] = L[i - 1][j - 1] + 1
                    print(i-1,j-1)
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])
        for i in range(l+1):
            print(L[i])
        return L[l][l]


obj = Solution()
print(obj.LongestRepeatingSubsequence("axxxy"))