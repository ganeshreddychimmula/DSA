'''
 Rotate Image

'''
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        #is if n is odd middle element doesn't change
        for i in range(n//2):
            for j in range(i,n-1-i):
                matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i]=matrix[n-1-j][i],matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j]
        '''for i in range(n):
            print(matrix[i])'''
        return matrix.copy()
obj = Solution()
arr=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
for i in range(len(arr)):
    print(arr[i])
arr=obj.rotate(arr)
for i in range(len(arr)):
    print(arr[i])
    