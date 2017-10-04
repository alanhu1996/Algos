# Given a collection of distinct numbers, return all possible permutations.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permuteHelper(nums, cur, result = []):
            if(len(cur) == len(nums)):
                result.append(cur)
                return result
            for item in nums:
                if(item in cur):
                    continue
                permuteHelper(nums, cur + [item], result)
            return result
        return permuteHelper(nums, [])
