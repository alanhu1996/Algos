# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

from random import randint

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def shuffle(lo, hi, nums):
            for i in range(lo, hi + 1):
                swap(nums, i, randint(lo, hi))
                
        def swap(nums, i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            return nums
        
        def partition(nums, lo, hi):
            pivot = nums[hi]
            pivotIndex = lo
            for i in range(lo, hi):
                if nums[i] <= pivot:
                    swap(nums, i, pivotIndex)
                    pivotIndex += 1
            swap(nums, pivotIndex, hi)
            return pivotIndex
        
        def findHelper(lo, hi, nums, k):
            if lo > hi:
                return -1
            midIndex = partition(nums, lo, hi)
            if midIndex == k:
                return nums[midIndex]
            elif midIndex > k:
                # Shuffle to make runtime linear even at worst case.
                shuffle(lo, midIndex - 1, nums)
                return findHelper(lo, midIndex - 1, nums, k)
            else:
                # Shuffle to make runtime linear even at worst case.
                shuffle(midIndex + 1, hi, nums)
                return findHelper(midIndex + 1, hi, nums, k)
        return findHelper(0, len(nums) - 1, nums, len(nums) - k)
    
    