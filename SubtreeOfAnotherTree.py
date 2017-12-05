# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def checkEntireTree(s, t):
            if not s:
                return False
            if isSameTree(s, t):
                return True
            return checkEntireTree(s.left, t) or checkEntireTree(s.right, t)
        def isSameTree(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            
            return root1.val == root2.val and isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
        return checkEntireTree(s, t)