'''
Write an algorithm to find out next greater number to given number with the same set of digits Asked in : Morgan Stanley, Makemytrip, Amazon

Example:

Input 1:
A = [1, 2, 3]
Output 1:
[1, 3, 2]
Input 2:
A = [3, 2, 1]
Output 2:
[1, 2, 3]
Hint 1 : Start comparing from right most Integer value with left one
Hint2 : You need to find immediate higher Number from given number
'''
'''
This method only prints greatest number with immediately numbers'''
# Given number as int array, this function finds the
# greatest number and returns the number as integer
# we will use quicksort for this
def partition(array, start, end):
    pivot = array[end]
    index = start
    current = start
    # As currrent points each elements put all elements gretaer than pivot right side of index
    while current < end:
        # when element greater than pivot found at current
        # swap current and index element and increment index,current
        if array[current] > pivot:
            array[current], array[index] = array[index], array[current]
            index += 1
        current += 1
    # by the time while ends index points to end or pivot element
    # by this time all elements below index would be greater than pivot so swap end and index
    array[end], array[index] = array[index], array[end]
    # we return index position as it acts as partition point in dividing array
    return index


def quicksort(array, start, end):
    if end > start:
        pi = partition(array, start, end)
        quicksort(array, start, pi - 1)
        quicksort(array, pi + 1, end)
    number=array[:]


def findNextNumber(number, n):
    # Practise Yourself :  Write your code Here
     quicksort(number, 0, n - 1)


digits = "218765"

number = list(map(int, digits))
findNextNumber(number, len(digits))
print(number)