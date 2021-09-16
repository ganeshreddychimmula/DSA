'''
Majority Element
BOYER MOORE VOTING ALGORITHM
https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1#
'''


def majorityElement(A, N):
    # Your code here
    majority = -1
    count = 1
    for i in range(0, N, 1):
        if A[i] == majority:
            count += 1
        else:
            count -= 1
        if count == 0:
            majority = A[i]
            count = 1
        # print(i, majority, count)
    # checking if majority number is more than n/2 times in array
    count = 0
    for i in range(0, N, 1):
        if A[i] == majority:
            count += 1
        if count > N / 2:
            return majority
    else:
        return -1


arr=[2, 3, 3, 5, 3]
print(majorityElement(arr, len(arr)))