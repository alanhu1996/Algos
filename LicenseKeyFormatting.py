# You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

# Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

# Given a non-empty string S and a number K, format the string according to the rules described above.
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        cur = []
        result = []
        for i in range(len(S) - 1, -1, -1):
            if S[i] == '-':
                continue
            if len(cur) == K:
                result.append(''.join(cur))
                cur = []
            cur.append(S[i].upper())
        
        result.append(''.join(cur))
        return '-'.join(result)[::-1]
        
        