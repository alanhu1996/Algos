# Find the sum of all left leaves in a given binary tree.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftNode = root.left
        addValue = 0
        if leftNode and not leftNode.left and not leftNode.right:
            addValue = leftNode.val
        
        return addValue + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)