'''
Largest square formed in a matrix
https://practice.geeksforgeeks.org/problems/largest-square-formed-in-a-matrix0806/1#
'''
class Solution:
    def maxSquare(self, n, m, mat):
        mx = 0  # max sum
        # sm[i][j] is bottom right item containing size of a square with ones
        #sm = [[0] * m] * n
        '''dont ever use [[0]*m]*n to intialize array'''
        sm=[[0 for x in range(m)] for y in range(n)]
        # first row and column remain same
        sm[0]=mat[0]
        mx=max(mat[0])
        #copying 1st colum into sm
        for i in range(n):
            sm[i][0] = mat[i][0]
            mx=max(mx,mat[i][0])

        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j]:
                    sm[i][j] = min(sm[i - 1][j], sm[i][j - 1], sm[i - 1][j - 1]) + 1

                mx = max(mx, sm[i][j])
        return mx
obj=Solution()
arr= [[0, 1, 0, 1, 0, 1],
      [1, 0, 1, 0, 1, 0],
      [0, 1, 1, 1, 1, 0],
      [0, 0, 1, 1, 1, 0],
      [1, 1, 1, 1, 1, 1]]
print(obj.maxSquare(len(arr),len(arr[0]),arr))