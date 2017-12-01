# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total = [0]
        def helper(root, total):
            if not root:
                return 0
            leftChain = helper(root.left, total)
            rightChain = helper(root.right, total)
            
            leftChain = leftChain + 1 if root.left and root.val == root.left.val else 0
            rightChain = rightChain + 1 if root.right and root.val == root.right.val else 0
            total[0] = max(total[0], leftChain + rightChain)
            return max(leftChain, rightChain)
        helper(root, total)
        return total[0]