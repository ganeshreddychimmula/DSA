'''
maximum pairwise product
'''

def maxproduct( arr, n ):
    if len(arr)==1:
        return arr[0],0
    elif len(arr) == 2:
        if arr[0]>arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]
    else:
        arr1 = arr[:n//2]
        arr2 = arr[n//2:]
        amax1, amax2 = maxproduct(arr1, len(arr1))
        bmax1, bmax2 = maxproduct(arr2, len(arr2))
        max1 = max(amax1, bmax1)
        max2 = max(bmax1, amax2, bmax2) if max1==amax1 else max(amax1, amax2, bmax2)
        return max1, max2



n = int(input())
arr = list(map(int, input().strip().split()))
max2, max1 = maxproduct(arr, n)
print(max1*max2)
'''
4
30 10 35 20
8
3 8 6 5 4 1 2 7
'''