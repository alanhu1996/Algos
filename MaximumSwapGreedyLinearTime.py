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
        
        bucket = [-1] * 10
        stringNum = str(num)
        for i in range(len(str(num))):
            bucket[int(str(stringNum[i]))] = i

        for i in range(len(stringNum)):
            for s in range(len(bucket) - 1, int(stringNum[i]), -1):
                if bucket[s] != -1 and bucket[s] > i and s > int(stringNum[i]):
                    return swap(num, bucket[s], i)                    
        
            
        return num
        
            