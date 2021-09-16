import sys
# equal number of rows and columns
def Min(arr,end):
    n=len(arr)
    mn=sys.maxsize
    for i in range(end):
        for j in range(end):
            mn=min(mn , arr[i][j])
    return mn
def Max(arr,start):
    n=len(arr)
    mx=-sys.maxsize-1
    for i in range(start,n,1):
        for j in range(start,n,1):
            mx=max(mx,arr[i][j])
    return mx
def findMaxdifference(arr,n):
    maxdiff=0
    ''' i1,j1 goes from 0,0 to n-2,n-2 -> block 1
        i2,j2 goes from i+1,j+1 to n-1,n-1-> block 2
        find minimum value in i1 and maximum value n i2
    '''
    for i in range(n-1):
        mn=Min(arr,i)
        mx=Max(arr,i+1)
        maxdiff=max(maxdiff,mx-mn)
    if maxdiff>0:
        return maxdiff
    else:
        return -1

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