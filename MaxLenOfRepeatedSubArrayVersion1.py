# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

# O(n^2) runtime, O(n^2) space. Timed out on the last test case on leetcode.

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0 for i in range(len(A) + 1)] for j in range(len(B) + 1)]
        maxLen = 0
        for i in range(len(A) + 1):
            for j in range(len(B) + 1):
                if i != 0 and j != 0 and A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    maxLen = max(dp[i][j], maxLen)
        return maxLen