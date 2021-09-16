'''
maximum rectangle
https://leetcode.com/problems/maximal-rectangle/submissions/
incomplete
'''
class Solution:
    def maximalRectangle(self, matrix):
        if matrix==[]:
            return 0
        n=len(matrix)
        m=len(matrix[0]) if n>0 else 0
        maxarea=0
        #input is given in strings
        for i in range(n):
            for j in range(m):
                matrix[i][j]=int(matrix[i][j])
        # param[height,width]
        param=[[[0,0] for j in range(m)] for i in range(n)]
        rect=[[[0,0] for j in range(m)] for i in range(n)]
        # copying the the parameters of top left item
        param[0][0]=rect[0][0]=[matrix[0][0],matrix[0][0]]
        maxarea=matrix[0][0]
        # calculating height and width for each matrix element considering it as bottom right part of an 'L' shape
        # calculating parameters of first row
        for j in range(1,m):
            param[0][j][0]=rect[0][j][0]=matrix[0][j] # height
            param[0][j][1]=rect[0][j][1]=param[0][j-1][1]+1 if matrix[0][j]==1 else 0 # width
            maxarea=max(maxarea,rect[0][j][1])
        # calculating param of first column
        for i in range(1,n):
            param[i][0][0]=rect[i][0][0]=param[i-1][0][0]+1 if matrix[i][0]==1 else 0 #height
            param[i][0][1]=rect[i][0][1]=matrix[i][0] #width
            maxarea = max(maxarea, rect[i][0][0])
        for i in range(1,n): # O(m*n)
            for j in range(1,m):
                param[i][j]=[param[i-1][j][0]+1,param[i][j-1][1]+1] if matrix[i][j]==1 else [0,0]
        # rect[0][1]=[5,5]
        '''for i in range(n):
            print(param[i],rect[i])'''
        # calculating rectangle and area
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]==0:
                    rect[i][j]=[0,0]
                    area=0
                # if height or width equals one rectangle == rect[i][j]
                elif param[i][j][0]==1 or param[i][j][1]==1:
                    rect[i][j]=param[i][j]
                    area=(param[i][j][0])*(param[i][j][1])
                else:#both width and height are greater than 1
                    if rect[i-1][j-1][0]>=param[i][j][0]-1 and rect[i-1][j-1][1]>=param[i][j][1]-1:
                        rect[i][j]=param[i][j]
                        area=param[i][j][0]*param[i][j][1]
                    else:# rect[i-1][j-1][0]<param[i][j][0]-1 or rect[i-1][j-1][1]<param[i][j][1]-1
                        rect[i][j][0]=rect[i-1][j-1][0] + 1 if rect[i-1][j-1][0]<param[i][j][0] else param[i][j][0]
                        rect[i][j][1]=rect[i-1][j-1][1] + 1 if rect[i-1][j-1][1]<param[i][j][1] else param[i][j][1]
                        area=max(param[i][j][0],param[i][j][1],(rect[i][j][0]*rect[i][j][1]))
                if area>maxarea:
                    maxarea=area
        for i in range(n):
            print(param[i],rect[i])
        return maxarea
obj=Solution()
#arr=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#arr=[[0,1]]
#arr=[[0,0,1],[1,1,1]]
arr=[["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],
     ["0","1","1","1","1","1"],["1","1","0","1","1","1"]]
print(obj.maximalRectangle(arr))