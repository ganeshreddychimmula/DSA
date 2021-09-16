'''

'''


def matrixRotation(matrix):
    end=len(matrix)-1
    n=len(matrix)
    i=j=0
    for i in range(n//2):#if len is odd  enter element need not to be changed
        for j in range(i,n-1-i):#left(that is i) to right-1
            matrix[i][j],matrix[j][end-i],matrix[end-i][end-j],matrix[end-j][i]=\
                matrix[end-j][i],matrix[i][j],matrix[j][end-i],matrix[end-i][end-j]

    for i in range(n):
        print(matrix[i])

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
matrixRotation(matrix)