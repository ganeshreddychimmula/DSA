'''
next largest number
https://leetcode.com/problems/next-permutation/
'''
def nextPermutation(nums):
    n = len(nums)
    left = 0
    # traversing from right to left in serch of number next to local maxima
    for i in range(n - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            left = i - 1
            break
    else:  # occurs when no greater number can be occured
        nums.sort()
        return nums
    min_greater = nums[left + 1]
    right = left + 1
    for i in range(left + 1, n, 1):
        if nums[i] > nums[left] and nums[i] < min_greater:
            right = i
            min_greater = nums[i]
    # swap left and right
    nums[left], nums[right] = nums[right], nums[left]
    # we have to sort all elements after left
    # we use insertion sort:
    print(left,right)
    for i in range(left + 2, n, 1):
        print(i)
        temp = nums[i]
        j = i-1
        while j > left and temp < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = temp
    return nums

nums=[7,2,3,4,7,6,5,4,3,2,1]
print(nextPermutation(nums))