# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

import statistics

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        
        median = statistics.median_high(nums)
    
        def swap(i, j, nums):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            return nums
        
        def reIndex(index):
            return (index * 2 + 1) % (len(nums) | 1)
        
        lower = 0
        i = 0
        upper = len(nums) - 1
        while(i <= upper):
            if nums[reIndex(i)] > median:
                swap(reIndex(lower), reIndex(i), nums)
                lower += 1
                i += 1
            elif nums[reIndex(i)] < median:
                swap(reIndex(i), reIndex(upper), nums)
                upper -= 1
            else:
                i += 1