# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        dp[0][0] = grid[0][0]
        for row in xrange(len(grid)):
            for col in xrange(len(grid[0])):
                if row == 0 and col == 0:
                    continue
                if row == 0:
                    dp[row][col] = dp[row][col - 1] + grid[row][col]
                elif col == 0:
                    dp[row][col] = dp[row - 1][col] + grid[row][col]
                else:
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]
        return dp[len(grid) - 1][len(grid[0]) - 1]