# Given a string s, find the longest palindromic subsequence's length in s. 
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[None for x in range(len(s))] for y in range(len(s))]
        
        def palinHelper(start, end, s, dp):
            if(dp[start][end] != None):
                return dp[start][end]
            if(end < start):
                return 0
            if(start == end):
                return 1
            if(s[start] == s[end]):
                dp[start][end] = palinHelper(start + 1, end - 1, s, dp) + 2
            else:
                dp[start][end] = max(palinHelper(start + 1, end, s, dp), palinHelper(start, end - 1, s, dp))
            return dp[start][end]
        return palinHelper(0, len(s) - 1, s, dp)