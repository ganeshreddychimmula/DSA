'''
Left Side More Right Side Less
Asked In: AmazonAkamaiJ P Morgan
We have an array, we have to find an element before which all elements are less than it,
and after which all are greater than it.
Finally, return the index of the element, if there is no such element, then return -1:
Time complexity O(n) and Space Complexity O(n)
Example:
Input: arr[] = {5, 1, 4, 3, 6, 8, 10, 7, 9};
Output: 4
Explanation: All elements on the left of arr[4] are smaller than it
and all elements on right are greater.
'''

import unittest

def findElement(array, n):
    #putting max value in left side of an element in left array
    #putiing min value in righ side of an element in an array
    left = [-9999] * n#just for the sake of left and rightmost elements during comparision
    right = [9999] * n
    i = 0
    max = array[0]
    for i in range(n):
        # max values for each elements
        left[i] = max
        if array[i] > max:
            max = array[i]
    min = array[n - 1]
    for i in range(n - 1, -1, -1):
        right[i] = min
        if array[i] < min:
            min = array[i]
    for i in range(n):
        if array[i] > left[i] and array[i] < right[i]:
            return i
    else:
        return -1


# ok for all test cases required
class Test(unittest.TestCase):
    def test_findElement1(self):
        actual = findElement([5, 1, 4, 3, 6, 8, 10, 7, 9], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_findElement2(self):
        actual = findElement([6, 2, 5, 4, 7, 9, 11, 8, 10], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_findElement3(self):
        actual = findElement([5, 1, 4, 4], 4)
        expected = -1
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)