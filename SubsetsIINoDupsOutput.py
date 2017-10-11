# Given a collection of integers that might contain duplicates, nums, return all possible subsets.

# Note: The solution set must not contain duplicate subsets.
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numsSorted = sorted(nums)
 
        def subsetsHelper(nums, cur, start, result = []):
            result.append(cur)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subsetsHelper(nums, cur + [nums[i]], i + 1, result)
            return result
        
        return subsetsHelper(numsSorted, [], 0)