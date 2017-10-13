# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i]
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)
        tmp = 1
        for i in range(1, len(nums)):
            output[i] = tmp * nums[i - 1]
            tmp = output[i]
        tmp = 1
        for i in range(len(nums) - 2, -1, -1):
            output[i] *= nums[i + 1] * tmp
            tmp *= nums[i + 1]
        return output