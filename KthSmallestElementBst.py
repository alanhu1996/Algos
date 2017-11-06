# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def dfs(root, count=[]):
            if not root:
                return count
            dfs(root.left, count)
            count.append(root.val)
            dfs(root.right, count)
            return count
        return dfs(root)[k - 1]

        # Basically passing k by reference to store the in order decrements properly.
        def dfsSpaceEfficient(root, k):
            if not root:
                return root
            left = dfs(root.left, k)
            k[0] -= 1
            if k[0] == 0:
                return root.val
            right = dfs(root.right, k)
            return left if left != None else right