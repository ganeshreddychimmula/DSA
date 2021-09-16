'''
https://www.youtube.com/watch?v=-7pzsM6gxgY
quicksort with last element as pivot
'''
import random
#quick sort
def partition(sample, start, end):
     print("sample=", sample)
     pivot = sample[end]
     #all elements left of index will be less than pivot
     index = start
     current = start
     while (current < end):
        if( sample[current] <= pivot):
            sample[index], sample[current] = sample[current], sample[index]
            index += 1
        current += 1
     sample[end], sample[index] = sample[index], sample[end]
     print("partitioned=", sample)
     return index


def quickSort(sample, start, end):
    if(start < end):
       index = partition(sample, start, end)
       quickSort(sample, start, index-1)
       quickSort(sample, index+1, end)


sample1 = random.sample(range(0,1000),10)
quickSort(sample1,0,9)