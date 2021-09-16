'''
Maximum Value in an array of Increasing and Decreasing using Binary Search
Asked In: AmazonMicrosoftUber
One array of integers is given as an input ,which is initially increasing and then decreasing or it can be only increasing or decreasing , you need to find the maximum value in the array in O(Log n) Time complexity and O(1) Space Complexity Asked in: Amazon, Microsoft, Uber

Example:

Input: array[] = {3, 5,15, 50, 11, 10, 8, 6}
Answer: 50
Hint: Think of using Binary Search
Problem level: Medium
'''

def findMaxValue(array, start, end):
    # first special case where number of elements in array is one
    if start == end:
        return array[start]
    # second special case when number of elements in array is two only
    if end == start + 1:
        if array[start] > array[end]:
            return array[start]
        else:
            return array[end]
    mid = (end + start) // 2
    # if mid element is top element
    if array[mid] > array[mid + 1] and array[mid] > array[mid - 1]:
        return array[mid]
    # if mid is on strictly increasing side ignore left and search right side
    if array[mid] > array[mid - 1] and array[mid] < array[mid + 1]:
        return findMaxValue(array, mid + 1, end)
    # if mid is on strictly increasing side ignore left and search right side
    if array[mid] < array[mid - 1] and array[mid] > array[mid + 1]:
        return findMaxValue(array, start, mid-1)


array = [3, 5, 15, 50, 11, 10, 8, 6]
n = len(array)
print("The maximum element is ", findMaxValue(array, 0, n - 1))
