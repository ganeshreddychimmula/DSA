'''
Maximum Rectangular Area in a Histogram
https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1#
Approach 2
'''
# importing stack
# from queue import LifoQueue
class Solution:
    def getMaxArea(self, histogram):
        n=len(histogram)
        maxarea=0
        stack=[]
        leftb=[0]*n#left boundary
        rightb=[0]*n# right boundary
        # Finding first smaller element on left for each bar
        for i in range(n):
            if not stack:
                stack.append(i)
                leftb[i]=0
            else:
                # delete elements from stack till current is greater than top element of stack or stack becomes empty
                while stack and (histogram[stack[-1]]>=histogram[i]):
                    stack.pop()
                # now element at top of stack is less than current element
                if not stack:
                    leftb[i]=0
                else:
                    leftb[i]=stack[-1]+1
                stack.append(i)
        #emptying stack for reuse
        stack=[]
        #finding first smaller element on right of each bar
        for i in range(n-1,-1,-1):
            if not stack:
                rightb[i]=n-1
                stack.append(i)
            else:
                while stack and (histogram[stack[-1]]>=histogram[i]):
                    stack.pop()
                if not stack:
                    rightb[i]=n-1
                else:
                    rightb[i]=stack[-1]-1
                stack.append(i)
        print(leftb,rightb)
        maxarea=0
        for i in range(n):
            area=histogram[i]*(rightb[i]-leftb[i]+1)
            if area>maxarea:
                maxarea=area
        return maxarea








obj=Solution()
#arr=[6,2,5,4,5,1,6]
#arr=[7 ,2 ,8 ,9 ,1 ,3 ,6 ,5]
arr=[1,2,3,4,5]
print(obj.getMaxArea(arr))