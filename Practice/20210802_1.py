'''
Ternary search
https://www.tutorialspoint.com/Ternary-Search
'''
def ternarysearch(arr,k,start,end):
    if start<=end:
        mid1 = start + (end - start)//3
        mid2 = end - (end-start)//3
        if arr[mid1]==k:
            return mid1
        if arr[mid2]==k:
            return mid2
        if arr[mid1]>k:
            return ternarysearch(arr,k,start,mid1-1)
        elif arr[mid2]<k:
            return ternarysearch(arr,k,mid2+1,end)
        else:
            return ternarysearch(arr,k,mid1,mid2)
    else:
        print(" given value is not in array")
        return None

arr = [12, 25, 48, 52, 67, 79, 88, 93]
print(ternarysearch(arr,93,0,len(arr)-1))