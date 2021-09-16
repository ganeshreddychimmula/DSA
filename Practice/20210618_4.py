'''
LB’s List : Merge Intervals
https://leetcode.com/problems/merge-intervals/
just works , bad logic time consuming
'''
from collections import defaultdict

def merge(intervals):
    dic=defaultdict(int)
    intervals.sort()
    n=len(intervals)
    for i in range(n):#used to check if range is already taken
        dic[i]=1#ok
    for i in range(n):
        for j in range(i+1,n,1) :
            if dic[j]==1 and intervals[i][1]>=intervals[j][0]:
                intervals[i][1]=max(intervals[i][1],intervals[j][1])
                dic[j]=-1
    dup=[]
    for i in range(n):
        if dic[i]==1:
            dup.append(intervals[i])
    return dup

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
'''
expected output:[[1,6],[8,10],[15,18]]
'''