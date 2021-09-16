'''
Longest repeating subsequence
https://practice.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1
'''

def lcs(X,Y,m,n):
    if m==0 or n==0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1+lcs(X,Y,m-1,n-1)
    else :
        return max(lcs(X,Y,m-1,n),lcs(X,Y,m,n-1))


X = "AGGTAB"
Y = "GXTXAYB"
# lcs is "GTAB"
print(lcs(X,Y,len(X),len(Y)))