'''
Techniques to print matrix in spiral order without any extra space
Asked In: MicrosoftOLAPayTmOracle
you are given a matrix of m x n elements (m rows, n columns),
 Print all elements of the matrix in spiral order in O(m*n) Time Complexity and O(1) Space Complexity Asked in: Microsoft, OLA, PayTm, Oracle

Example:

Input:
[
[ 1, 2, 3 ],
[ 4, 5, 6 ],
[ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Hint 1 : Divide the matrix in different layers and print numbers from outer to inner layer
'''
def spiralPrint(m, n, matrix):
    # Practise Yourself :  Write your code Here
    left = 0  # left position
    right = m-1  # top position
    upper=0
    lower=n-1

    array = []
    while left < right and upper < lower:
        #print("p,m,n,k",p,m,n,k)
        # upper part of layer
        i = upper  # fixed
        for j in range(left,right,1):
            #print(i,j)
            array.append(matrix[i][j])
        # right part of layer
        j = right  # fixed
        for i in range(upper,lower,1):
            #print(i, j)
            array.append(matrix[i][j])
        # bottom part of layer
        i = lower  # fixed
        for j in range(right,left, -1):
            #print(i, j)
            array.append(matrix[i][j])
        # left part of layer
        j = left  # fixed
        for i in range(lower, upper, -1):
            #print(i, j)
            array.append(matrix[i][j])
        #print("end of one layer")
        left+= 1
        upper+= 1
        right -= 1
        lower -= 1
    print(array)


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

R = 4
C = 4
spiralPrint(R, C, matrix)