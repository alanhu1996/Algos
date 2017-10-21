# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def swap(i, j):
            tmp = i
            i = j
            j = tmp
            return (i, j)
        curMax = nums[0]
        curMin = nums[0]
        maxProduct = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                curMax, curMin = swap(curMax, curMin)
            curMax = max(curMax * nums[i], nums[i])
            curMin = min(curMin * nums[i], nums[i])
            maxProduct = max(curMax, maxProduct)
            
        
        return maxProduct       
            
        