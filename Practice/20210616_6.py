"""
Maximum and minimum of an array using minimum number of comparisons
https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/
"""
#Tournament Method
def Max(a,b):
    if a>b:
        return a
    else:
        return b
def Min(a,b):
    if a>b:
        return b
    else:
        return a

def getMinMax(low,high,arr):
    max=arr[low]
    min=arr[low]

    if low==high:#if there is only one element left
        max=arr[low]
        min=arr[low]
        return (max,min)
    elif high==low+1:#if there are only two elements left
        if arr[low]>arr[high]:
            return (arr[low],arr[high])
        else:
            return (arr[high],arr[low])
    else:
        mid=(low+high)//2
        max1,min1=getMinMax(low,mid,arr)
        max2,min2=getMinMax(mid+1,high,arr)
    return (Max(max1,max2),Min(min1,min2))

# Driver code
arr = [1000, 11, 445, 1, 330, 3000]
high = len(arr) - 1
low = 0
arr_max, arr_min = getMinMax(low, high, arr)
print('Minimum element is ', arr_min)
print('nMaximum element is ', arr_max)