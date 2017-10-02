# Given an unsorted array of integers, find the length of longest increasing subsequence.
# Runtime: O(n^2)

# The runtime can be optimized to log(n) with binary search.

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        
        for upper in range(len(nums)):
            for lower in range(upper):
                if(nums[lower] < nums[upper]):
                    if(dp[lower] + 1 > dp[upper]):
                        dp[upper] = dp[lower] + 1

        return max(dp) if dp != [] else 0