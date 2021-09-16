'''
i1,j1 goes from 0,0 to n-2,n-2 -> block 1
i2,j2 goes from i+1,j+1 to n-1,n-1-> block 2
find minimum value in i1 and maximum value n i2
intuition:
We are create a matrix to hold maximum values from end of each row
for every element in block 1 we just search first column in block2 of maximum matrix
considering maxm[i][j] as top-left element of block b we put max of that block there
'''
import sys
def findMaxdifference(arr,n):
    mxdiff=0
    mx = -sys.maxsize-1
    maxm = [[0]*n for i in range(n)]
    #because we block 2 doesn't include row1
    for i in range(n-1,0,-1):
        mx=arr[i][n-1]
        for j in range(n-1,-1,-1):
            mx=max(mx,arr[i][j],arr[i+1][j]) if i+1 < n else max(mx,arr[i][j])
            maxm[i][j]=mx
    for i in range(n):
        print(maxm[i])
    for i in range(n-1):
        for j in range(n-1):
            mn=arr[i][j]
            mx=maxm[i+1][j+1]
            mxdiff=max(mxdiff,mx-mn)

    return mxdiff


n=int(input())
arr=[[0]*n for i in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().strip().split()))
print(findMaxdifference(arr,n))
'''for i in range(n):
    print(arr[i])'''
'''
inputs:

3
1 2 3
4 5 6
7 8 9
3
-1 -2 -3
-4 -5 -6
-7 -8 -9
2
1 5 
4 2 
3
-1 5 -3
-14 -5 -2
-7 8 -9

'''