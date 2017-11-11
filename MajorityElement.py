# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Based on the majority vote algorithm: https://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                count += 1
                majority = nums[i]
            elif nums[i] == majority:
                count += 1
            else:
                count -= 1
        return majority