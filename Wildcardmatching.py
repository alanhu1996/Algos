# Implement wildcard pattern matching with support for '?' and '*'.

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sIndex = 0
        pIndex = 0
        isStar = -1
        matched = 0
        while sIndex < len(s):
            if pIndex < len(p) and (p[pIndex] == '?' or s[sIndex] == p[pIndex]):
                sIndex += 1
                pIndex += 1
                continue
            
            elif pIndex < len(p) and p[pIndex] == '*':
                isStar = pIndex
                matched = sIndex + 1
                pIndex += 1
                continue
                
            elif isStar != -1:
                sIndex = matched
                matched += 1
                pIndex = isStar + 1
                continue
            
            return False
            
        while pIndex < len(p) and p[pIndex] == '*':
            pIndex += 1
        
        return pIndex == len(p)
                