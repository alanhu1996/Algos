# Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

# You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

# Return the maximum profit you can make.

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buyChoice = -prices[0]
        buySellChoice = 0
        
        for i in range(1, len(prices)):
            # Only sell and buy if it makes the current total profit increase.
            buySellChoice = max(buySellChoice, prices[i] + buyChoice - fee)
            # Only buy if if we end up keeping more money than the original buy choice at the previous price.
            buyChoice = max(buyChoice, buySellChoice - prices[i])
        
        return buySellChoice