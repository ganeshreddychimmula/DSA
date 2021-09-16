'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
'''
'''
[1,3,5,6]
5
constraint: time complexity == O(logn)
'''
def binarySearch(ar,l,r,s):
    '''if l==r:
        return l'''

    mid=l+(r-l)//2
    #print("l=%d r=%d mid=%d"%(l,r,mid))
    if l>r:
        return -1
    if ar[mid]==s:
        return mid
    elif l==r :
        if ar[r]>s:
            return r
        elif ar[r]<s:
            return r+1 #if it is greater last number
    elif ar[mid]<s and ar[mid+1]>s:
        return mid+1
    elif ar[mid]>s:
        return binarySearch(ar,l,mid-1,s)
    else :
        return binarySearch(ar,mid+1,r,s)


arr=list(map(int,input().lstrip("[").rstrip("]").split(",")))
s=int(input())
#print(type(arr),arr[0],arr,s)
print(binarySearch(arr,0,len(arr)-1,s))
#print(len(arr)-1)