class Solution:
    def first(self, a, low, high):
        if low <= high:
            mid = (low + high) // 2
            # if start element encountered
            if (mid == 0 or a[mid - 1] == 0) and a[mid] == 1:
                return mid
            elif a[mid] == 0:
                return self.first(a, mid + 1, high)
            else:
                return self.first(a, low, mid - 1)
        return -1  # no 1 found

    def rowWithMax1s(self, arr, n, m):
        index = self.first(arr[0], 0, m - 1)
        count = m - index if index != -1 else 0
        column_index = 0
        max_ones = count
        # print(0,index,count)
        for i in range(1, n):
            index = self.first(arr[i], 0, m - 1)
            count = m - index if index != -1 else 0
            # print(i,index,count)
            if count > max_ones:
                column_index = i
                max_ones = count

        if max_ones > 0:
            return column_index
        else:
            return -1

obj=Solution()
arr=[[0, 1, 1, 1],
           [0, 0, 1, 1],
           [1, 1, 1, 1],
           [0, 0, 0, 0]]
print(obj.rowWithMax1s(arr,len(arr),len(arr[0])))