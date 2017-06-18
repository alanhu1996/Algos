# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSoFar = maxCurrent = nums[0]
        for i in range(1, len(nums)):
            maxCurrent = max(nums[i], maxCurrent + nums[i])
            # The maxSoFar variable will contain the max sum of the array up to i - 1 index. It will be updated by comparing with the sum of the array at ith index.
            maxSoFar = max(maxSoFar, maxCurrent)
        return maxSoFar