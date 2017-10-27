# Given two strings s and t, write a function to determine if t is an anagram of s.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashDictS = {}
        hashDictT = {}
        if len(s) != len(t):
            return False
        for c in s:
            hashDictS[str(c)] = 0 if str(c) not in hashDictS else hashDictS[str(c)] + 1
        for c in t:
            hashDictT[str(c)] = 0 if str(c) not in hashDictT else hashDictT[str(c)] + 1
        return hashDictT == hashDictS