class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = [{} for i in range(len(nums))] 

        def dfs(pathLength, currentSum, nums, target, total=[0]):
            if pathLength == len(nums) and currentSum == target:
                return 1
            elif pathLength == len(nums):
                return 0
            if currentSum in dp[pathLength]:
                return dp[pathLength][currentSum]
            
            add = dfs(pathLength + 1, currentSum + nums[pathLength], nums, target)  
            sub = dfs(pathLength + 1, currentSum - nums[pathLength], nums, target)
            dp[pathLength][currentSum] = add + sub
            return dp[pathLength][currentSum]
        return dfs(0, 0, nums, S)