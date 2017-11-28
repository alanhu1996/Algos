class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        if sum(nums) % k != 0:
            return False
        
        visited = [False] * len(nums)
        
        def dfs(currentSum, currentSetSize, k, startIndex, visited, target, nums):
            # Since we know that the total sum is divisible by target. If there is only one partition left to check, we know for sure it is equal to target.
            if k == 1:
                return True
            # No need to traverse this branch if size is already greater than target.
            if currentSum > target:
                return False
            # If sum is target, then we move onto the next state which is with k - 1 partitions to find.
            if currentSum == target and currentSetSize > 0:
                return dfs(0, 0, k - 1, 0, visited, target, nums)
            for i in range(startIndex, len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                # Go to the next state, which is taking the next element, increasing the current set size and the current sum.
                if dfs(currentSum + nums[i], currentSetSize + 1, k, i + 1, visited, target, nums):
                    return True
                visited[i] = False
            return False
        return dfs(0, 0, k, 0, visited, sum(nums) / k, nums)