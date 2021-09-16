'''
Fractional knapsack
https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
'''
class Solution:
    # partition of quicksort
    def partition(self, Items, low, high):
        # function to ease val per weight calculation
        def wv(obj):
            return (obj.value) / (obj.weight)
        # function used to swap item places
        def swap(Items, i1, i2):
            a = Items[i1]
            b = Items[i2]
            a.weight, a.value, b.weight, b.value = b.weight, b.value, a.weight, a.value
            Items[i1] = a
            Items[i2] = b
            return Items

        pivot = wv(Items[high])
        current = index = low
        while current < high:
            if wv(Items[current]) < pivot:
                Items = swap(Items, current, index)
                index += 1
            current += 1
        Items = swap(Items, index, high)
        return Items, index

    # quick sort is used for sorting as they mentioned constant space
    def objsort(self, Items, low, high):
        if low < high:
            Items, pi = self.partition(Items, low, high)
            self.objsort(Items, low, pi - 1)
            self.objsort(Items, pi + 1, high)
        return Items

    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W, Items, n):
        i = 0
        V = 0 # total value of knapsack
        # sort items according to value per weight ratio
        Items = self.objsort(Items, 0, n - 1)
        # from item starting from highest val per weight ratio put into knapsack
        for j in range(n - 1, -1, -1):
            i = Items[j]
            if W > 0:
                # a is the used to calculate fraction of item weight kept in knapsack
                a = min(W, i.weight)
                V += a * (i.value / i.weight)
                W -= a
                # print(i.weight, i.value, a, V)
            else:
                break
        # print(W,Items[0].value,n)
        return V
        # code here


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


if __name__ == '__main__':
        n, W = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        Items = [Item(0, 0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2 * i]
            Items[i].weight = info[2 * i + 1]

        ob = Solution()
        print("%.2f" % ob.fractionalknapsack(W, Items, n))
'''
input format:
n knapsackcapacity
value weight pairs
'''
# } Driver Code Ends
'''
3 50
60 10 100 20 120 30 
expected output: 240
3 50
60 10 120 30 100 20
'''
