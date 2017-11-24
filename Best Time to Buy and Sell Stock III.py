# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most two transactions.

# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        MAX_TRANSACTIONS = 2
        if len(prices) == 0:
            return 0
        dp = [[0 for i in range(len(prices))] for j in range(MAX_TRANSACTIONS + 1)]
        for i in range(1, MAX_TRANSACTIONS + 1):
            tempMax = dp[i - 1][0] - prices[0]
            for j in range(1, len(prices)):
                # Do nothing this day or sell depending on which one makes the most money.
                dp[i][j] = max(dp[i][j - 1], tempMax + prices[j])
                # We want to buy the stock on the day which we end up with the most money after the purchase.
                tempMax = max(tempMax, dp[i - 1][j] - prices[j])
                # Update max profit.
                maxProfit = max(maxProfit, dp[i][j])
        return maxProfit