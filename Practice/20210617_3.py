'''
Minimum number of jumps
https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1#
'''
def minJumps( arr, n):
    cladder =arr[0]
    sladder = arr[0]
    jump = 1
    for i in range(1, n):
        cladder -= 1
        sladder -= 1
        if cladder == -1:
            return -1
        if i == n - 1:
            print(i, cladder, sladder)
            return jump
        if arr[i] > sladder:
            sladder = arr[i]
        if cladder == 0 and sladder != 0:
            cladder = sladder
            jump += 1
        print(i, cladder , sladder)
arr=[2,1,0,3]
print(minJumps(arr,len(arr)))
