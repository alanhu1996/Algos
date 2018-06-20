# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def modBinarySearch(start, end, target):
            if start > end:
                return -1
            mid = start + (end - start) / 2
            if target == nums[mid]:
                return mid
            
            # Right side is sorted
            if nums[mid] < nums[end]:
                if target > nums[mid] and target <= nums[end]:
                    return modBinarySearch(mid + 1, end, target)
                else:
                    return modBinarySearch(start, mid - 1, target)
            else:
                if target >= nums[start] and target < nums[mid]:
                    return modBinarySearch(start, mid - 1, target)
                else:
                    return modBinarySearch(mid + 1, end, target)
        return modBinarySearch(0, len(nums) - 1, target)
                