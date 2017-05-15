class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        output = []
        for i in range(len(nums)):
            # Duplicate check for the i pointer.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            leftPointer, rightPointer = i + 1, len(nums) - 1
            if(leftPointer == len(nums)):
                continue
            while(leftPointer < rightPointer):
        
                sum = nums[leftPointer] + nums[rightPointer] + nums[i]
                if sum < 0:
                    leftPointer += 1
                elif sum > 0:
                    rightPointer -= 1
                else:
                    output.append([nums[leftPointer], nums[i], nums[rightPointer]])
                    # Duplicate check for the left pointer.
                    while leftPointer < rightPointer and nums[leftPointer] == nums[leftPointer + 1]:
                        leftPointer += 1
                    # Duplicate check for the right pointer.
                    while leftPointer < rightPointer and nums[rightPointer] == nums[rightPointer - 1]:
                        rightPointer -= 1
                    leftPointer += 1
                    rightPointer -= 1
        return output

solution = Solution()
print(solution.threeSum([0, 0, 0, 0]))