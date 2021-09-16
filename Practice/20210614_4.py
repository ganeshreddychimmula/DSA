'''
Linear time approach to solve Stock Buy Sell Problem
Asked In: AmazonMicrosoftFlipkartDE-Shaw
An array is given as Input where ith element is the price of a given stock on day You were permitted to complete unlimited transaction.
 Derive an algorithm to find the maximum profit in O(n) Time complexity and O(n) Space Complexity
Asked in: Amazon, Microsoft, Flipkart, DE-Shaw
Example:
Input: [7,1,5,3,6,4]
Input: [7,6,4,3,1]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 2 (price = 5) and Buy on day 3 (price = 3) and
 sell on day 4 (price = 4),  profit = (5-1) + (6-3) = 7.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Hint 1:  find out the maximum difference (which will be the maximum profit) between two numbers in the given array
Hint2: You need to solve this problem in O(n) time complexity
'''

# find local minima an dlocal maxima and then subtract them
def findProfit(array, n):
    profit = 0
    total = 0
    localmin = 0
    localmax = 0
    for i in range(n):
        if localmin == 0 and array[i] < array[i + 1]:
            localmin = array[i]
            continue
        if localmax == 0 and i == (n - 1):
            localmax = array[i]

        if localmax == 0 and array[i] > array[i + 1]:
            localmax = array[i]
        if localmin != 0 and localmax != 0:
            profit = localmax - localmin
            total += profit
            localmax = localmin = 0

    return total

if __name__ == '__main__':
    price = [98, 178, 250, 300, 40, 540, 690];
    n = len(price);
    print(findProfit(price, n))
