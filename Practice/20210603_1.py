'''
insertion sort gfg practice problem
https://practice.geeksforgeeks.org/problems/insertion-sort/1
'''


class Solution:
    def insert(self, alist, index, n):
        j = index
        while alist[j - 1] > alist[j] and j > 0:  # if current key is less than predecessor key swap
            temp = alist[j]
            alist[j] = alist[j - 1]
            alist[j - 1] = temp
            j -= 1  # decrement j

    # Function to sort the list using insertion sort algorithm.
    def insertionSort(self, alist, n):
        for i in range(1, n):
            if alist[i] < alist[i - 1]:
                self.insert(alist, i, n)
        stri = ' '.join(map(str, alist))
        return stri

    # {


#  Driver Code Starts
if __name__ == "__main__":
        n = int(input())
        arr = list(map(int, input().split()))
        z=Solution().insertionSort(arr, n)

        print(z)
# } Driver Code Ends
'''
input:
10
10 9 8 7 6 5 4 3 2 1
'''