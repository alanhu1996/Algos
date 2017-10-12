# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

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
            # The tree could have repeating values, so we have to compare the entire node.
            if root == None or root == p or root == q:   
                return root
            
            left = lcaHelper(root.left, p, q)  
            right = lcaHelper(root.right, p, q)
                
            return root if left and right else left or right
        
        return lcaHelper(root, p, q)