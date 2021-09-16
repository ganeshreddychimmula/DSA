'''
Maximum Rectangular Area in a Histogram
https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1#
'''
#divide and conquer approach
class Solution:
    def Smallest(self, a, low, high):
        index = low
        for i in range(low, high + 1):
            if a[i] < a[index]:
                index = i
        return index

    def mergesort(self, arr, low, high):
        if low == high:
            # if len ==1 return height of arr
            return arr[low]

        if high == low + 1:
            small = min(arr[low], arr[high])
            return max(arr[low], arr[high], 2 * small)
        # index of smallest bar
        smallest = self.Smallest(arr, low, high)
        print(smallest)
        maxleft = maxright = mergedmax = 0
        if smallest > low and smallest <= high:
            maxleft = self.mergesort(arr, low, smallest - 1)
        if smallest < high and smallest>=low:
            maxright = self.mergesort(arr, smallest + 1, high)
        #high - low + 1 gives length of sub array
        mergedmax = (arr[smallest]) * (high - low + 1)

        return max(maxleft, maxright, mergedmax)

        # Function to find largest rectangular area possible in a given histogram.

    def getMaxArea(self, histogram):
        n = len(histogram)
        return self.mergesort(histogram, 0, n - 1)

obj=Solution()
arr=[6,2,5,4,5,1,6]
arr=[7 ,2 ,8 ,9 ,1 ,3 ,6 ,5]
print(obj.getMaxArea(arr))