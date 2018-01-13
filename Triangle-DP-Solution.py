# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
		# Bottom up 1D dynamic programming solution.
		dp = list(triangle[len(triangle) - 1])
		for row in xrange(len(triangle) - 1 - 1, -1, -1):
		    for col in xrange(len(triangle[row])):
		        dp[col] = min(dp[col], dp[col + 1]) + triangle[row][col]
		return dp[0]