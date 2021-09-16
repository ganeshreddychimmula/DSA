'''
Min Steps in Infinite Grid

https://www.interviewbit.com/problems/min-steps-in-infinite-grid/
'''


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def distance(self, x1, y1, x2, y2):
        x = abs(x1 - x2)
        y = abs(y1 - y2)
        return max(x, y)

    def coverPoints(self, A, B):
        n = len(A)
        steps = 0
        for i in range(n - 1):
            steps += self.distance(A[i], B[i], A[i + 1], B[i + 1])
        return steps

obj=Solution()
A=[1,-5]
B=[-7,-13]
print(obj.coverPoints(A,B))
