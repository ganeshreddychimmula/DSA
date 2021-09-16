'''
Buy and sell stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
from collections import defaultdict


class Solution:
    def maxProfit(self, prices) :
        d = defaultdict(list)
        n = len(prices)
        max_sum = 0
        mn = prices[0]
        mx = prices[n - 1]
        diff = 0

        # finding minimum for all elements
        for i in range(n):
            if prices[i] < mn:
                mn = prices[i]
            d[i].append(mn)

        for i in range(n - 1, -1, -1):
            if prices[i] > mx:
                mx = prices[i]
            d[i].append(mx)
        for i in d.values():
            diff = i[1] - i[0]
            if diff > max_sum:
                max_sum = diff

        if max_sum > 0:
            return max_sum
        else:
            return 0

prices = [7,1,5,3,6,4]
obj=Solution()
print(obj.maxProfit(prices))