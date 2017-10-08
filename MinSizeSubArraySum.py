# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        # Recursive solution, not very efficient and currently buggy. Quadratic runtime.
        def minHelper(s, curLen, nums, start, end):
            if s < 0 or start > end:
                return curLen
            
            return min(minHelper(s - sum(nums[start:end]), curLen + 1, nums, start + 1, end), minHelper(s - sum(nums[start:end]), curLen + 1, nums, start, end - 1))
                
        #return minHelper(s, 0, nums, 0, len(nums))
        

        # Iterative solution, linear runtime. Works well and very fast.
        def minHelperIter(s, nums):
            start, end, curSum = 0, 0, 0
            minLen = len(nums) + 1
            for end in range(len(nums)):  
                curSum += nums[end]
                while(curSum >= s):
                    # end + 1 - start is the current sub array size.
                    minLen = min(minLen, end + 1 - start)
                    curSum -= nums[start]
                    start += 1
                
            return minLen if minLen < len(nums) + 1 else 0
        return minHelperIter(s, nums)
                
                