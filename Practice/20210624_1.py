'''
Spirally traversing a matrix
https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1
'''
class Solution:

    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix, r, c):
        spiral = []
        n = r  # height
        m = c
        i = 0
        j = 0
        while i < n - 1 - i and j < m - 1 - j:
            # top layer

            h = i
            for w in range(j, m - 1 - j,1):
                spiral.append(matrix[h][w])
            # right layer
            w = m - 1 - i
            for h in range(i, n - 1 - i,1):
                spiral.append(matrix[h][w])
            # bottom layer
            h = n - 1 - i
            for w in range(m - 1 - j, j, -1):
                spiral.append(matrix[h][w])
            # left layer
            w = j
            for h in range(n - 1 - i, i, -1):
                spiral.append(matrix[h][w])
            j += 1
            i += 1
        #column j==m-1-j is left
        if i<n-1-i and j==m-1-j:
            w=m-1-j
            for h in range(i,n-i,1):
                spiral.append(matrix[h][w])
        # row i==n-1-i is left
        if j<m-1-j and i==n-1-i:
            h=n-1-i
            for w in range(j,m-j,1):
                spiral.append(matrix[h][w])
        # middle element is left behind
        if i == n - 1 - i and j == m - 1 - j:
            spiral.append(matrix[i][j])
        return spiral

rc="3 5"
inp="6 6 2 28 2 12 26 3 28 7 22 25 3 4 23"
r,c=map(int,rc.strip().split())
values=list(map(int,inp.strip().split()))
k=0
matrix=[]
for i in range(r):
    row=[]
    for j in range(c):
        row.append(values[k])
        k+=1
    matrix.append(row)
obj=Solution()
print(obj.spirallyTraverse(matrix,r,c))