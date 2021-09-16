'''
 Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
Find the maximum profit you can achieve. You may complete at most two transactions.
'''


class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        #used to keep track of profits
        profit = [0] * n
        mx = prices[n - 1]
        mn = prices[0]
        #calculating max profit in sub array i.....n-1
        for i in range(n - 2, -1, -1):
            if prices[i] > mx:
                mx = prices[i]
            profit[i] = max(profit[i + 1], mx - prices[i])
        #calcualting max profit in sub array 0....i
        for i in range(1, n, 1):
            if prices[i] < mn:
                mn = prices[i]
            profit[i] = max(profit[i - 1], profit[i] + (prices[i] - mn))
        result = profit[n - 1]
        return result

obj=Solution()
arr=[3,3,5,0,0,3,1,4]
print(obj.maxProfit(arr))