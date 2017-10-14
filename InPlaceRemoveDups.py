# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, 0
        if len(nums) == 0:
            return 0
        while(end < len(nums)):
            if nums[start] == nums[end]:
                end += 1
            else:
                start += 1
                nums[start] = nums[end]
                end += 1
        return start + 1