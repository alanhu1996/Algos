# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        def dpSolution(coins, amount, dp):
            for i in range(1, amount + 1):
                for j in range(len(coins)):
                    if coins[j] <= i:
                        dp[i] = min(dp[i], dp[i - coins[j]] + 1)
            return dp[amount] if dp[amount] <= amount else -1
            
        def recursionSolution(coins, amount, dp):
            if amount == 0:
                return 0
            elif amount < 0:
                return -1
            
            if dp[amount - 1] != 0:
                return dp[amount - 1]
            minNum = -1 
            for i in xrange(len(coins)):
                result = recursionSolution(coins, amount - coins[i], dp)
                if result != -1 and (result < minNum or minNum == -1):
                    minNum = 1 + result

            dp[amount - 1] = minNum
            return dp[amount - 1]
        

        return dpSolution(coins, amount, dp)
                