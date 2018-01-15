# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Linear runtime, linear space.
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        cumulativeSum = 0
        # Need to have a zero sum here to account for total - k = 0.
        totalSumDict = {0: 1}
        totalSubArrays = 0
        for i in range(len(nums)):
            cumulativeSum += nums[i]
            differenceKey = cumulativeSum - k
            if differenceKey in totalSumDict:
                totalSubArrays += totalSumDict[differenceKey]
            totalSumDict[cumulativeSum] = 1 if cumulativeSum not in totalSumDict else totalSumDict[cumulativeSum] + 1

        return totalSubArrays