# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        maximumResult = -1
        def swap(num, n, m):
            stringNum = list(str(num))
            temp = stringNum[n]
            stringNum[n] = stringNum[m]
            stringNum[m] = temp
            result = 0
            for numIterate in stringNum:
                result = int(numIterate) + result
                result = result * 10
            return result / 10
        
        for i in range(len(str(num))):
            for s in range(i, len(str(num))):
                maximumResult = max(maximumResult, swap(num, i, s))
        return maximumResult
        
            