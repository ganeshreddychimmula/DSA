'''
Count frequencies of array elements in O(n) time complexity
Asked In: PayTmVmWareAmazon
Array of length n having integers 1 to n with some elements being repeated.
Count frequencies of all elements from 1 to n in Time Complexity O(n) and Space Complexity O(1) Asked in : : PayTm, VmWare, Amazon
Example:
Input array elements: 5, 1, 2, 5, 5, 5, 1, 1, 2, 2
Output
Frequency of 5 = 4
Frequency of 2 = 3
Frequency of 1 = 3
Hint1 : All the numbers are between 1 to n in the given array
Hint2: Think of updating index of array for given number
'''


def printfrequency(arr, n):
    # decrementing each element in array by 1
    for i in range(n):
        arr[i] -= 1

    # traversing through array and for every element get it's actual value(that is before adding n)
    # add n to corresponding index element
    actual = 0
    for i in arr:
        actual = i % n
        arr[actual] += n
    # printing the frequencies
    for i in range(n):
        freq = arr[i] // n
        if freq > 0:
            print("%d : %d" % (i + 1, freq))


arr = [5, 1, 2, 5, 5, 5, 1, 1, 2, 2]
n = len(arr)
printfrequency(arr, n)



