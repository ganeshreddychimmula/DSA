'''
maximum rectangle
https://leetcode.com/problems/maximal-rectangle/submissions/

'''


class Solution:
    def maxhistogramarea(self, arr, m):
        stack = []
        leftb = [0] * m
        rightb = [0] * m
        maxarea = 0
        for i in range(m):
            # if stack empty
            if not stack:
                stack.append(i)
                leftb[i] = stack[-1]
            else:
                # delete elements till current element is greater than top element of stack ,
                # also stop if it becomes empty
                while stack != [] and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                # left boundary is right to next smaller element on left or at start if no smaller exists
                leftb[i] = stack[-1] + 1 if stack != [] else 0
                stack.append(i)
        stack = []
        for i in range(m - 1, -1, -1):
            if not stack:
                rightb[i] = m - 1
                stack.append(i)
            else:
                # delete elements till current element is greater than top element of stack
                # also stop if it becomes empty
                while stack != [] and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                # right boundary is left to next smaller element on right or at end if no smaller exists
                rightb[i] = stack[-1] - 1 if stack != [] else m - 1
                stack.append(i)
        # rightb[i]-leftb[i]+1 gives width
        for i in range(m):
            maxarea = max(maxarea, arr[i] * (rightb[i] - leftb[i] + 1))
        # print(arr,leftb,rightb)
        return maxarea

    # take each row as a histogram
    def maximalRectangle(self, matrix ):
        if matrix == []:
            return 0
        n = len(matrix)
        m = len(matrix[0]) if n > 0 else 0
        maxarea = 0
        # input is given in strings
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])
        # heights
        heights = [[0 for j in range(m)] for i in range(n)]
        # heights of row 0
        heights[0] = matrix[0]
        maxarea = max(matrix[0])
        # heights of rest of the matrix rows
        for i in range(1, n):
            for j in range(m):
                if matrix[i][j]:
                    heights[i][j] = heights[i - 1][j] + 1
                    maxarea = max(maxarea, heights[i][j])
                # else it remains zero
        for i in range(n):
            maxarea = max(maxarea, self.maxhistogramarea(heights[i], m))
        '''for i in range(n):
            print(heights[i])'''

        return maxarea
obj=Solution()
#arr=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#arr=[[0,1]]
#arr=[[0,0,1],[1,1,1]]
arr=[["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],
     ["0","1","1","1","1","1"],["1","1","0","1","1","1"]]
print(obj.maximalRectangle(arr))