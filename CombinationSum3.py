# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        upperLimit = 9
        lowerLimit = 1
        def helper(currentSize, path, startIndex, currentSum, maxSize, target, result=[]):
            if currentSize == maxSize and currentSum == target:
                result.append(path)
                return result
            for i in range(startIndex, upperLimit + 1):
                helper(currentSize + 1, path + [i], i + 1, currentSum + i, maxSize, target, result)
            
            return result
        return helper(0, [], lowerLimit, 0, k, n)
                