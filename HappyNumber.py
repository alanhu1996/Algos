# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def addDigs(num):
            result = 0
            while num > 0:
                result += (num % 10) * (num % 10)
                num /= 10
            return result
        fast = n
        slow = n
        # Add the digits.
        # Detect cycles.
        while True:
            fast = addDigs(fast)
            fast = addDigs(fast)
            slow = addDigs(slow)
            if(fast == slow):
                break
        return slow == 1