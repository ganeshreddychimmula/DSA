'''
Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
'''
class Solution:
    def searchMatrix(self, matrix,target):
        i=0
        m=len(matrix)#height
        n=len(matrix[0])#width
        j=n-1
        while j>=0 and i<=m-1:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                j-=1
            else:
                i+=1
        return False

obj=Solution()
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]

target=3
print(obj.searchMatrix(matrix,target))