# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        secondBound = len(nums) - 1
        zeroBound = 0
        for i in range(secondBound + 1):
            while(nums[i] == 2 and i < secondBound):
                swap(i, secondBound)
                secondBound -= 1
            while(nums[i] == 0 and i > zeroBound):
                swap(i, zeroBound)
                zeroBound += 1
       