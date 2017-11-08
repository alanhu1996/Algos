# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""
        else:
            return self.convertToTitle((n - 1) / 26) + chr((n - 1) % 26 + ord('A'))