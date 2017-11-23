# Given an integer, write a function to determine if it is a power of two.
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # All power of 2 numbers have only one bit that is 1.
        return n > 0 and (n & (n - 1)) == 0