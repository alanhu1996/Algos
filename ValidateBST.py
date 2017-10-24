# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValidHelper(root, minVal, maxVal):
            if root == None:
                return True

            if root.val <= minVal or root.val >= maxVal:
                return False

            return isValidHelper(root.left, minVal, root.val) and isValidHelper(root.right, root.val, maxVal)

        return isValidHelper(root, -sys.maxint - 1, sys.maxint)