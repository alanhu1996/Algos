# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfsSum(root, pathSum):
            if not root:
                return 0
            if not root.left and not root.right:
                return pathSum * 10 + root.val
            return dfsSum(root.left, pathSum * 10 + root.val) + dfsSum(root.right, pathSum * 10 + root.val)
            
        return dfsSum(root, 0)
            
        