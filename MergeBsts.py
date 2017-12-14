# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def helper(t1, t2):
            if not t1 and not t2:
                return None
            newNode = TreeNode(0)
            if t1 and t2:
                newNode.val = t1.val + t2.val
                newNode.left = helper(t1.left, t2.left)
                newNode.right = helper(t1.right, t2.right)
            elif t1:
                newNode.val = t1.val
                newNode.left = helper(t1.left, t2)
                newNode.right = helper(t1.right, t2)
            else:
                newNode.val = t2.val
                newNode.left = helper(t1, t2.left)
                newNode.right = helper(t1, t2.right)
            return newNode
        return helper(t1, t2)