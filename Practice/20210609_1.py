'''
Search an element in a sorted and rotated array
Asked In: LinkedinGoldman Sachs
We rotate an ascending order sorted array at some point unknown to user. So for instance, 3 4 5 6 7 might become 5 6 7 3 4.
 Modify binary search algorithm to find an element in the rotated array in O(log n) time and O(1) Space complexity
Example:

array[] = {3,4,5,6,7,8,9,10,1,2}
Search Number = 1
Output: 8
[Hint: Use Binary Search]
Problem level: Medium
'''

import unittest


# given array is in asending order
def findNumber(array, start, end, value):
    # Write your code here
    if start == end:
        if array[start] == value:
            return start
        else:
            return -1
    mid = (start + end) // 2
    if array[mid] == value:
        return mid
    # if true mean that left part is strictly increasing
    if array[mid] > array[start]:
        if array[start] <= value and array[mid] > value:
            return findNumber(array, start, mid - 1, value)
        else:
            return findNumber(array, mid + 1, end, value)
    else:  # mean right part is strictly increasing
        if array[mid] < value and array[end] >= value:
            return findNumber(array, mid + 1, end, value)
        else:
            return findNumber(array, start, mid - 1, value)


# ok for all test cases required
class Test(unittest.TestCase):

    def test_findNumber1(self):
        actual = findNumber([3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 0, 9, 1)
        expected = 8
        self.assertEqual(actual, expected)

    def test_findNumber2(self):
        actual = findNumber([5, 6, 7, 8, 9, 10, 1, 2, 3], 0, 8, 3)
        expected = 8
        self.assertEqual(actual, expected)

    def test_findNumber3(self):
        actual = findNumber([5, 6, 7, 8, 9, 10, 1, 2, 3], 0, 8, 28)
        expected = -1
        self.assertEqual(actual, expected)

    def test_findNumber4(self):
        actual = findNumber([30, 40, 50, 10, 20], 0, 4, 10)
        expected = 3
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)