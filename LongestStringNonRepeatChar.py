# Given a string, find the length of the longest substring without repeating characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dupDict = {}
        maxVal = 0
        lower = 0
        for upper in range(len(s)):
            if s[upper] in dupDict:
                lower = max(dupDict[s[upper]], lower)
            maxVal = max(upper - lower + 1, maxVal)
            dupDict[s[upper]] = upper + 1
        return maxVal