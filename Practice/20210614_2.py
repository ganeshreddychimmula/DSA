'''
Majority Number
Asked In: YahooLinkedin
Given an array of integer, write an efficient algorithm to find majority number in that array in Time Complexity O(n) and Space Complexity O(1)
Example:
[Majority Number : The only number in the integer array which appears more than n/2 times if the length of the array is n]
Input : [1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2 ]
Output: 2 ( 2 appears in this integer array more than 5 times]
[Hint: Think of using the hint, element appears more than half
'''

import unittest


# Function to return majority element present in given list
# majority number : The only number in the integer which appears more than n/2 times
# only one element can appear greater than n/2 times
def majorityElement(A):
    n = len(A)
    # decrementing each element by 1 to correspond to index’s
    for i in range(n):
        A[i] -= 1
    # traversing through array
    # updating indices by adding n to each respective indeces
    for i in A:
        actual = i % n  # number before upfates
        A[actual] += n

    for i in range(n):
        freq = A[i] // n
        if freq > n // 2:
            return i + 1

    return -1




# ok for all test cases required
class Test(unittest.TestCase):
    def test_majorityElement1(self):
        actual = majorityElement([1, 3, 3, 4, 3, 2, 2, 2, 2, 2, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_majorityElement2(self):
        actual = majorityElement([1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_majorityElement3(self):
        actual = majorityElement([3, 2, 3])
        expected = 3
        self.assertEqual(actual, expected)

    def test_majorityElement4(self):
        actual = majorityElement([2, 2, 1, 1, 1, 2, 2])
        expected = 2
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
