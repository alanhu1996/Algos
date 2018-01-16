# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        diffTable = {}
        def preOrderTraversal(root, k):
            if not root:
                return False

            diffKey = k - root.val
            if root.val in diffTable:
                return True
            else:
                diffTable[diffKey] = True

            return preOrderTraversal(root.left, k) or preOrderTraversal(root.right, k)
        return preOrderTraversal(root, k)

            
            