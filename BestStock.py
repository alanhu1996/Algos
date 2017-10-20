# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        minPrice = sys.maxint 
        for i in range(len(prices)):
            minPrice = min(prices[i], minPrice)
            maxProfit = max(maxProfit, prices[i] - minPrice)
        return maxProfit