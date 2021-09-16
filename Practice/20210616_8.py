'''
Move all negative elements to end
Given an unsorted array having both negative and positive integers.
The task is place all negative element at the end of array without changing the order of positive element and negative element.
https://practice.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1#
    
'''

def segregateElements(arr, n):
    # Your code goes here
    index = 0
    neg = []
    for i in range(n):
        if arr[i] < 0:
            neg.append(arr[i])
        else:
            arr[index] = arr[i]
            index += 1
    for i in neg:
        arr[index] = i
        index += 1

    return arr

arr=[1, -1, 3, 2, -7, -5, 11, 6]
print(segregateElements(arr,len(arr)))