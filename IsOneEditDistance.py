# Given two strings S and T, determine if they are both one edit distance apart.

class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) < len(s):
            return self.isOneEditDistance(t, s)
        if len(t) - len(s) > 1 or s == t:
            return False
        
        for i in range(len(s)):
            if s[i] != t[i]:
                if len(s) == len(t):
                    s = s[:i] + t[i] + s[i + 1:len(s)]
                else:
                    s = s[:i] + t[i] + s[i:len(s)]
                break
                
        return s == t or t[:-1] == s