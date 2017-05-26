# Reverse digits of an integer.

class Solution(object):
    # def reverse(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     result = 0
    #     isNegative = x < 0
    #     x = abs(x)
    #     while(x > 0):
    #         result = result * 10 + x % 10
    #         x = x / 10
            
    #     return -result if isNegative else result
    def reverse(self, x):
        print(sys.maxint)
        #Using max integer for c because leetcode doesn't accept python max integer.
        C_MAX_INT = 2147483647
        result = int(str(x)[::-1]) if x >= 0 else -1 * int(str(x)[1::][::-1])
        return result if result <= C_MAX_INT and result >= -C_MAX_INT + 1 else 0