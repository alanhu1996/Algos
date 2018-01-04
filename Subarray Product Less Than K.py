# Your are given an array of positive integers nums.

# Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        product = 1
        left, result = 0, 0
        for i in range(len(nums)):
            product *= nums[i]
            while product >= k:
                product /= nums[left]
                left += 1
            # This is the amount of continuous new sub arrays which can be formed with the new right index.
            result += i - left + 1
        return result