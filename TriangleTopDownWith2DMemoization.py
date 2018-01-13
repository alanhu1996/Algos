# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        # Top down recursion dfs with memoization.
        dp = [[None for i in range(len(triangle[len(triangle) - 1]))] for s in range(len(triangle))]
        def dfs(row, col, triangle, dp):
            if row == len(triangle) or col == len(triangle[row]):
                return 0
            if dp[row][col] != None:
                return dp[row][col]
            left = dfs(row + 1, col, triangle, dp)
            right = dfs(row + 1, col + 1, triangle, dp)
            dp[row][col] = min(left, right) + triangle[row][col]
            return dp[row][col]
        return dfs(0, 0, triangle, dp)