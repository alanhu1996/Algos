# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(start, end, nums):
            if start >= end:
                return None
            maxNumber = max(nums[start:end])
            maxNumberIndex = nums.index(maxNumber)
            
            root = TreeNode(maxNumber)
            root.left = helper(start, maxNumberIndex, nums)
            root.right = helper(maxNumberIndex + 1, end, nums)
            
            return root
        return helper(0, len(nums), nums)
            