# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 and n == 0:
            return 0
        dp = [[0 for s in range(m)] for t in range(n)]
        
        for row in range(len(dp)):
            for col in range(len(dp[0])):
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
                    
        return dp[n- 1][m - 1]