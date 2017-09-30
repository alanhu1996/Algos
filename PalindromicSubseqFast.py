class Solution(object):
    def longestPalindromeSubseq(self, s):
        
        def palinHelperFast(s):
            dp = [0] * len(s)
            for upper in range(0, len(s)):
                prev = 0
                # Any one letter is a palindrome.
                dp[upper] = 1
                for lower in range(upper - 1, -1, -1):
                    tmp = dp[lower]
                    
                    if(s[lower] == s[upper]):
                        dp[lower] = 2 + prev
                    else:
                        dp[lower] = max(dp[lower], dp[lower + 1])
                    prev = tmp
            return dp[0]
        return palinHelperFast(s)