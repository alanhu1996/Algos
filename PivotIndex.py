# Given an array of integers nums, write a method that returns the "pivot" index of this array.

# We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalLeft = 0
        total = sum(nums)
        for i in range(0, len(nums)):
            if totalLeft == total - totalLeft - nums[i]:
                return i
            totalLeft += nums[i]
            
        return -1
                                                    