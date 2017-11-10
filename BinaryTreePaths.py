# Given a binary tree, return all root-to-leaf paths.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def helper(root, curPath, result=[]):
            if not root.left and not root.right:
                result.append(curPath)
                return result
            if(root.left):
                helper(root.left, curPath + '->' + str(root.left.val), result)
            if(root.right):
                helper(root.right, curPath + '->' + str(root.right.val), result)
            return result
        return helper(root, str(root.val)) if root else []