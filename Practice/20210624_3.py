'''
https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1#

'''

class Solution:
    def median(self, matrix, r, c):
        low = 2000
        high = 1
        for i in range(c):
            high = max(high, matrix[i][c - 1])
        for i in range(r):
            low = min(low, matrix[i][0])
        desired = (r * c + 1) // 2
        # print(low,high)
        # return None
        while low <= high:
            count = 0
            mid = (low + high) // 2
            # counting number of number less than or equal to given number
            for i in range(r):
                for j in range(c):
                    if matrix[i][j] <= mid:
                        count += 1
                    else:
                        break

            if count == desired:
                return mid
            elif count < desired:
                low = mid + 1
            else:
                high = mid

        return low