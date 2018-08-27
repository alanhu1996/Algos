# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 1 5 8 4 7 6 5 3 1
        # 1 5 8 5 1 3 4 6 7
        def checkIfDigitIsDesc(digit, index):
            for i in range(len(nums) - 1, index, -1):
                if digit < nums[i]:
                    return i
            return -1
        
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        for i in range(len(nums) - 1, -1, -1):
            swapIndex = checkIfDigitIsDesc(nums[i], i)
            if swapIndex != -1:
                swap(swapIndex, i)
                nums[i + 1: len(nums)] = reversed(nums[i + 1: len(nums)])
                break
        if swapIndex == -1:
            nums.reverse()
                    