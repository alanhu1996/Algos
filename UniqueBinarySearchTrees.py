# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1
        
        # i can equal to n.
        for i in range(2, n + 1):
            # j can equal to i.
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]