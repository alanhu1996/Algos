# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]
        def dfs(root, result):
            if not root:
                return 0
            left = dfs(root.left, result)
            right = dfs(root.right, result)
            result[0] = max(result[0], left + right + 1)
            return max(left, right) + 1
        dfs(root, result)
        return result[0] - 1 if result[0] else 0