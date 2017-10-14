# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def lcaHelper(root, p, q):
            if not root or p.val < root.val < q.val or q.val < root.val < p.val or root.val == p.val or root.val == q.val:
                return root 
            
            return lcaHelper(root.right, p, q) or lcaHelper(root.left, p, q)
        
        return lcaHelper(root, p, q)