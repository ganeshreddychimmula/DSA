'''
logic mojo arrays
Segregation logic to Sort an array of 0's, 1's and 2's
Array consist of only 0's, 1's and 2's. Write an algorithm to sort  this array in O(n) time complexity and O(1) Space complexity with only one traversal Asked in : : Amazon, Microsoft, Adobe, WalmartLabs

Example:

Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]
Hint1 : You are not suppose to use any extra space
Hint2 : You need change the same array with single traversal with O(n) time complexity
'''


# Function to swap two elements array[i] and array[j] in the list
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


# sort a list containing 0, 1 and 2
# three-way Partitioning
#it is similar to insertion sort
# we first traverse through array keeping all elements smaller than pivot=1 before i
#later we traverse back from end with c2 pointer putting all elements greater than pivot after j
def sort012(array, end):
    i = 0
    j = end
    c1 = 0  # c1
    c2 = end  # c2
    pivot = 1
    # putting all o's in array before i
    while c1 <= end:
        if array[c1] < pivot:
            swap(array, c1, i)
            i += 1
        c1 += 1
    # print(i)
    # putting all 2's in array after j
    while c2 >= i:
        if array[c2] > pivot:
            swap(array, c2, j)
            j -= 1
        c2 -= 1
    # print(j)
    return array


if __name__ == '__main__':
    array = [2, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    sort012(array, len(array) - 1)
    print(array)