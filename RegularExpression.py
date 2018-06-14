# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == "" and p == "":
            return True
        
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(len(s) + 1):
            for j in range(1, len(p) + 1):
                if j > 1 and p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (i > 0 and (p[j - 2] == s[i - 1] or p[j - 2] == '.') and dp[i - 1][j])
                else:
                    dp[i][j] = i > 0 and dp[i - 1][j - 1] and (p[j - 1] == s[i - 1] or p[j - 1] == '.')
        return dp[len(s)][len(p)]