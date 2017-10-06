# Given two binary trees, write a function to check if they are equal or not.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def isSameTreeHelper(p, q):
            if(p == None and q == None):
                return True
            if(p == None or q == None):
                return False
            return p.val == q.val and isSameTreeHelper(p.left, q.left) and isSameTreeHelper(p.right, q.right)
        return isSameTreeHelper(p, q)