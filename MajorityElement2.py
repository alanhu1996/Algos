# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Run a two majority version of Boyer-Moore Majority Vote algorithm.
        counter1 = 0
        counter2 = 0
        majority1 = 0
        majority2 = 1
        for i in range(len(nums)):
            if majority1 == nums[i]:
                counter1 += 1
            elif majority2 == nums[i]:
                counter2 += 1
            elif counter1 == 0:
                majority1 = nums[i]
                counter1 += 1
            elif counter2 == 0:
                majority2 = nums[i]
                counter2 += 1
            else:
                counter1 -= 1
                counter2 -= 1
        # Make sure the count of each majority is greater than the floor of length of nums / 3.
        return [n for n in (majority1, majority2) if nums.count(n) > len(nums) // 3]