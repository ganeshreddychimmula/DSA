'''
https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1#
'''
def findTwoElement(arr, n):
    # code here
    res = [None, None]
    # numbers are in range(1,N) we bring them to (0,N-1) range
    for i in range(n):
        arr[i] -= 1
    for i in range(n):
        arr[arr[i] % n] += n
    for i in range(n):
        # missing element
        if arr[i] // n == 0:
            res[1] = i + 1
        elif arr[i] // n == 2:
            res[0] = i + 1
    return res

arr1=[1, 3, 3]
arr = [5, 3, 2, 2, 1]
res=findTwoElement(arr, len(arr))
print("%d is missing number"%res[1])
print("%d is repeating number number"%res[0])