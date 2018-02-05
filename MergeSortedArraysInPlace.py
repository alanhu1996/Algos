# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        topIndex = m + n - 1
        
        n1Index = m - 1
        n2Index = n - 1
        while n2Index >= 0:
            # We check n1Index >= 0 because of the case of n1 running out before n2.
            if nums1[n1Index] > nums2[n2Index] and n1Index >= 0:
                nums1[topIndex] = nums1[n1Index]
                n1Index -= 1
            else:
                nums1[topIndex] = nums2[n2Index]
                n2Index -= 1
            topIndex -= 1
            
        