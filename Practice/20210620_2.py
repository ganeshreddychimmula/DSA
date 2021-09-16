'''

'''


class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self, arr, n):
        prod = max_prod = 1
        neg = 0
        for i in range(n):
            if arr[i] == 0:
                prod = 1
                # if x=zero is encountered then from right of zero we get first
                # neagtive number
                neg = 0
                continue
            # we just consider first negative number
            if neg == 0 and arr[i] < 0:
                # product upto first negative in the sub array
                neg = prod*arr[i]
            #product of all terms after last zero was encountered
            prod *= arr[i]
            # if temp prod seem to be negative then divide it by
            # product until first negative occurrence in sub array
            if prod < 0:
                if (prod//neg) > max_prod:
                    max_prod = prod//neg
                # print(prod)
            if prod > max_prod:
                max_prod = prod
            #print(prod)
        return max_prod
obj=Solution()
arr=[0, 3, -5, -2 ,8 ,-7, -6, -2, -3 ,-9,]
print(obj.maxProduct(arr,len(arr)))