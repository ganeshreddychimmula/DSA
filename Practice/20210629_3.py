'''
maximum rectangle
https://leetcode.com/problems/maximal-rectangle/submissions/

'''


class Solution:
    def maxhistogramarea(self, arr, m, i):
        stack = []
        maxarea = 0
        current = 0
        while current < m:
            if (not stack) or arr[stack[-1]] <= arr[current]:
                stack.append(current)
                current += 1
            else:  # if stack[-1]>arr[current]
                base = stack.pop()
                '''if stack not empty width = (next smaller on right(that is current))-next smaller on 
                left(that is present top of stack = stack[-1]) - 1 ;
                else there is no smaller element on left current gives width'''
                area = arr[base] * (current - stack[-1] - 1 if stack else current)
                maxarea = max(maxarea, area)
            # print(stack,i)
        '''For remaining elements in stack pop each element and use m as right most boundary as 
        for each top element no smaller element exists on right'''

        while stack:  # while stack not empty
            base = stack.pop()
            area = arr[base] * (m - stack[-1] - 1 if stack else m)
            # m for smallest element
            maxarea = max(maxarea, area)
        return maxarea

    # take each row as a histogram
    def maximalRectangle(self, matrix):
        if not matrix:  # if matrix empty
            return 0
        n = len(matrix)
        m = len(matrix[0]) if n > 0 else 0
        maxarea = 0
        # heights
        heights = [[0 for j in range(m)] for i in range(n)]
        # input is given in strings
        for i in range(n):
            for j in range(m):
                if i == 0:  # row 1
                    heights[i][j] = int(matrix[i][j])
                else:
                    if int(matrix[i][j]) == 0:
                        heights[i][j] = 0
                    else:
                        heights[i][j] = heights[i - 1][j] + 1
                maxarea = max(maxarea, heights[i][j])

        for i in range(n):
            maxarea = max(maxarea, self.maxhistogramarea(heights[i], m, i))
        '''
        for i in range(n):
            print(heights[i])
        '''
        return maxarea

obj=Solution()
#arr=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#arr=[[0,1]]
#arr=[[0,0,1],[1,1,1]]
arr=[["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],
     ["0","1","1","1","1","1"],["1","1","0","1","1","1"]]
print(obj.maximalRectangle(arr))