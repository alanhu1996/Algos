# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        # The idea is to start at each center and expand out wards for even and odd length substrings.
        def sumPalindromes(boundLow, boundHigh, word):
            total = 0
            while boundLow >= 0 and boundHigh < len(word) and word[boundLow] == word[boundHigh]:
                total += 1
                boundLow -= 1
                boundHigh += 1
            return total
                
        total = 0

        for i in range(len(s)):
            total += sumPalindromes(i, i, s)
            total += sumPalindromes(i, i + 1, s)
        return total