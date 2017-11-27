class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # We sort so we get get the duplicate values side by side.
        sortedList = sorted(nums)
        used = [False] * len(nums)
        def permute(used, path, nums, result = []):
            if len(path) == len(nums):
                result.append(path)
                return result
            for i in range(len(nums)):
                if used[i]:
                    continue
                # Duplicate check. We only take one version of the duplicate ordering.
                if i > 0 and nums[i - 1] == nums[i] and not used[i - 1]:
                    continue
                used[i] = True
                permute(used, path + [nums[i]], nums, result)
                used[i] = False
            return result
        return permute(used, [], sortedList)