# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        
        while(left < right):
            sumNum = numbers[left] + numbers[right]
            if sumNum == target:
                # Returning non zero based indices.
                return [left + 1, right + 1]
            elif sumNum > target:
                right -= 1
            else:
                left += 1
        return -1