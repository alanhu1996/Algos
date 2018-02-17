# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, len(s) + 1):
            twoPrev = s[i - 2] + s[i - 1]

            if 1 <= int(s[i - 1]) <= 9:
                dp[i] = dp[i - 1]
                
            if 10 <= int(twoPrev) <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]