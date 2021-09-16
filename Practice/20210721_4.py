'''
https://practice.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1#
https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
'''
# Dynamic Programming implementation of LCS problem

def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    for i in range(m+1):
        print(L[i])
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


# end of function lcs


# Driver program to test the above function
Y = "AGGTAB"
X = "GXTXAYB"
print("Length of LCS is ", lcs(X, Y))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
