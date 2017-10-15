# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def bstHelper(lower, upper, nums):
            mid = (lower + upper) / 2
            if lower > upper:
                return None
            
            root = TreeNode(nums[mid])
            root.left = bstHelper(lower, mid - 1, nums)
            root.right = bstHelper(mid + 1, upper, nums)
            
            return root
        return bstHelper(0, len(nums) - 1, nums)