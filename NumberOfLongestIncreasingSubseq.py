# Given an unsorted array of integers, find the number of longest increasing subsequence.

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        result = 0
        longestSoFar = [1] * len(nums)
        lengthCount = [0] * len(nums)
        for i in range(len(nums)):
            lengthCount[i] = 1
            for j in range(0, i):
                if(nums[i] > nums[j]):
                    if longestSoFar[j] + 1 == longestSoFar[i]:
                        lengthCount[i] += lengthCount[j]
                    elif longestSoFar[j] + 1 > longestSoFar[i]:
                        longestSoFar[i] = longestSoFar[j] + 1 
                        lengthCount[i] = lengthCount[j]
            if maxLen == longestSoFar[i]:
                result += lengthCount[i]
            elif maxLen < longestSoFar[i]:
                result = lengthCount[i]
                maxLen = longestSoFar[i]
        return result