"""
Remove Duplicate From String
String is given as input that contains only lowercase letters,
remove duplicate letters so that every letter appears once In O(n) Time Complexity and O(1) Space Complexity\
Example:
Input: "bcabc"
Input: "cbacdcbc"
Output: "bca"
Output: "cbad"
Hint : Try using ascii[256] array for storing ascii value of the character
"""
def removeDuplicatesFromString(str2):
    l = len(str2)
    arr=list(str2)
    array=[0]*266#independent of lngth of string so constant space
    for i in range(l):
        num=ord(arr[i])
        if array[num]==0:
            array[num]=-1
        else:
            arr[i]=""
    str="".join(arr)
    return str



    #Write your Code here


#ok for all test cases required
import unittest
class Test(unittest.TestCase):
    def test_removeDuplicatesFromString1(self):
        actual = removeDuplicatesFromString('bcabc')
        expected = 'bca'
        self.assertEqual(actual, expected)

    def test_removeDuplicatesFromString2(self):
        actual = removeDuplicatesFromString('cbacdcbc')
        expected = 'cbad'
        self.assertEqual(actual, expected)

    def test_removeDuplicatesFromString3(self):
        actual = removeDuplicatesFromString('aabbccdef')
        expected = 'abcdef'
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)