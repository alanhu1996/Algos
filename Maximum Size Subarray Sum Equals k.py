# Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Greedy approach.
        valueTable = {}
        
        accSum = 0
        maxLength = 0
        for i in range(len(nums)):
            accSum += nums[i]
            if accSum not in valueTable:
                valueTable[accSum] = i
            
            if accSum == k:
                maxLength = i + 1
            elif accSum - k in valueTable:
                maxLength = max(maxLength, i - valueTable[accSum - k])
            
        return maxLength
        