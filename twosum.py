# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortedList = sorted(nums)
        #print(sortedList)
        left = 0;
        right = len(nums) - 1
        while(left < right):
            sum = sortedList[left] + sortedList[right]
            if(sum == target):
                    
                return [nums.index(sortedList[left]), nums.index(sortedList[right]) if sortedList[right] != sortedList[left] else [i for i, n in enumerate(nums) if n == sortedList[right]][1]]
            elif(sum < target):
                left += 1
            else:
                right -= 1
            
        return []