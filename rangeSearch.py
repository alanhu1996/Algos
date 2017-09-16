# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def searchIndexHelper(nums, target, getLowest):
            # Initialize pointer variables for binary search.
            low = 0
            hi = len(nums) - 1
            mid = -1
            result = -1
            while(low <= hi):
                mid = (low + hi) / 2
                if(nums[mid] > target):
                    hi = mid - 1
                elif(nums[mid] < target):
                    low = mid + 1
                else:
                    result = mid
                    # Found the number. Now look for the first or last.
                    if(getLowest):
                        if(mid == 0 or nums[mid - 1] != nums[mid]):
                            break
                        hi = mid - 1
                    else:
                        if(mid == len(nums) - 1 or nums[mid + 1] != nums[mid]):
                            break
                        low = mid + 1
            return result
        return [searchIndexHelper(nums, target, True), searchIndexHelper(nums, target, False)]
            
                