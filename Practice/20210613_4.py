'''
Print Matrix Diagonally
Asked In: FacebookCitrixFlipkart
Given a matrix of M x N elements (M rows, N columns), Print all elements of the matrix in diagonal order in Time Complexity O(m*n) and Space Complexity O(1)
Expected Output
1
6 2
11 7 3
16 12 8 4
17 13 9 5
18 14 10
19 15
20
'''


def diagonalPrint(matrix):
    i = 0
    j = 0
    lower = len(matrix) - 1
    right = len(matrix[0]) - 1
    array = []
    #traversing through first half of matrix
    # going upward diagonally
    # i is decreasing j is increasing
    for i in range(0,lower+1,1):
        while i>=0:
            #print(i, j)
            array.append(matrix[i][j])
            if i==0:
                j=0
                break
            if i>0:
                i-=1
                j+=1
    i=lower
    #print(i,j)
    for j in range(1,right+1,1):
        while j<=right:
            #print(i,j)
            array.append(matrix[i][j])
            if j==right:
                i=lower
                break
            if j<right:
                i-=1
                j+=1


    print(array)

matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20], ]
diagonalPrint(matrix)