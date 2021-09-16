'''
In-place techniques matrix rotation method by 90 degree
You are given a square matrix, You need to rotate the matrix in a clockwise direction by 90 degrees in Time Complexity O(m*n)
and No Extra Space i.e O(1) Asked in : Facebook, Google, Amazon, Microsoft
Example:
Input : 
If the array is
[
    [1, 2],
    [3, 4]
]
Output:
Rotated array becomes:
[
    [3, 1],
    [4, 2]
]
'''

#layer by layer approach
# In-place rotate it by 90 degrees in clockwise direction
def matrixRotation(matrix):
    i = j = a = b = 0  # i,j for original array a,b for rotated array
    left = 0
    right = len(matrix) - 1  # square matrix
    top = 0
    bottom = len(matrix) - 1
    rot = [[0]*len(matrix) for i in range(len(matrix))]
    while top<bottom and left<right:
        # top to right
        i = top
        a = top
        b = right
        for j in range(left, right, 1):  # left to right-1
            rot[a][b] = matrix[i][j]
            a += 1
        # right to bottom
        j = right
        a = bottom
        b = right
        for i in range(top, bottom, 1):
            rot[a][b] = matrix[i][j]
            b -= 1
        #bottom to right
        i=bottom
        a=bottom
        b=left
        for j in range(right,left,-1):
            rot[a][b]=matrix[i][j]
            a-=1
        #left to right
        j=left
        a=top
        b=left
        for i in range(bottom,top,-1):
            rot[a][b] = matrix[i][j]
            b+=1
        top-=1
        bottom+=1
        left+=1
        right-=1
    if len(matrix)%2!=0:
        a=len(matrix)//2
        rot[a][a]=matrix[a][a]
    for k in range(len(matrix)):
        print(rot[k])
    #print(matrix)


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

actual = matrixRotation(matrix)
print(actual)

