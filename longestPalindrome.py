# Given a string s, find the longest palindromic substring in s.

class Solution(object):
    
    def isPalindrome(self, s):
        return s == s[::-1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestLength = 0
        longestWord = ""
        for i in range(len(s)):
            lowerHigh = i - longestLength 
            lowerLow = i - longestLength - 1 
            upper = i + 1
            
            
            if(i + 1 <= len(s) and lowerHigh >= 0 and self.isPalindrome(s[lowerHigh: upper])):
                longestLength += 1
                longestWord = s[lowerHigh: upper]
                continue
                
            if(i + 1 <= len(s) and lowerLow >= 0 and self.isPalindrome(s[lowerLow: upper])):
                longestLength += 2
                longestWord = s[lowerLow: upper]
                continue
                
        return longestWord
            
                
            