# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.



class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def recursionSolution(currentIndex):
            if currentIndex == len(nums) - 1:
                return True
            maxHops = nums[currentIndex]
            result = False
            for i in range(1, maxHops + 1):
                result = result or recursionSolution(currentIndex + i)
            return result
        
        def dpSolution(startIndex):
            dp = [False] * len(nums)
            dp[len(nums) - 1] = True
            for i in xrange(len(nums) - 2, -1, -1):
                for j in xrange(1, nums[i] + 1):
                    currentIndex = i + j
                    if currentIndex >= len(nums):
                        continue
                    dp[i] = nums[currentIndex] >= len(nums) - 1 - currentIndex or dp[currentIndex]
                    if dp[currentIndex]:
                        break
            return dp[0]
        
        def greedySolution():
            lastGoodIndex = len(nums) - 1
            for i in range(len(nums) - 2, -1, -1):
                if nums[i] >= lastGoodIndex - i:
                    lastGoodIndex = i
            return lastGoodIndex == 0
        return greedySolution()
        # return dpSolution(len(nums) - 1)
                
        # return recursionSolution(0)
            