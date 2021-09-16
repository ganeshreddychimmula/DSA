'''
permutations of a given string
'''
import itertools


class Solution:
    def find_permutation(self, S):
        perms = [''.join(p) for p in itertools.permutations(S)]
        return sorted(perms)


obj = Solution()
print(obj.find_permutation("XYZ"))
