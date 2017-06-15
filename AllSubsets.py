# Given a set of distinct integers, nums, return all possible subsets.

# Note: The solution set must not contain duplicate subsets.

class Solution(object):
    def subsets(self, nums):
        def subsetsHelper(arr, depth, currSet = [], result = []):
            if(depth == len(arr) - 1):
                result.append(currSet)
                return result
            
            subsetsHelper(arr, depth + 1, currSet, result)
            subsetsHelper(arr, depth + 1, currSet + [arr[depth]], result)
            return result
            
        return subsetsHelper(nums, -1, [], [])
        