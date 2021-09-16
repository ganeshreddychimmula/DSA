'''
Matrix n*n is given, where all elements in any individual row or column are sorted.
In such a matrix, we have to find the position of a value in O(n) Time Complexity and O(1) Space Complexity
'''


def searchElement(matrix, n, x):
    found = False
    i = 0
    j = n - 1
    while found != True:
        if matrix[i][j] == x:
            return True
        elif matrix[i][j] > x and j > 0:
            j -= 1
        elif matrix[i][j] < x and i < n - 1:
            i += 1
        else:
            return False
    # Write your Code here


# ok for all test cases required
import unittest


class Test(unittest.TestCase):

    def test_searchElement_test1(self):
        actual = searchElement([[10, 20, 30, 40],
                                [15, 25, 36, 46],
                                [27, 29, 37, 48],
                                [32, 33, 39, 50]], 4, 32)
        expected = True
        self.assertEqual(actual, expected)

    def test_searchElement_test2(self):
        actual = searchElement([[10, 20, 30, 40],
                                [15, 25, 36, 46],
                                [27, 29, 37, 48],
                                [32, 33, 39, 50]], 4, 59)
        expected = False
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)