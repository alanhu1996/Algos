# You are given a binary tree in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def traverseEachNode(root, target):
            if not root:
                return 0
            return getPathSum(root, target) + traverseEachNode(root.left, target) + traverseEachNode(root.right, target)
        
        def getPathSum(root, currentSum):
            if not root:
                return 0
            totalCount = 1 if currentSum == root.val else 0
            return totalCount + getPathSum(root.left, currentSum - root.val) + getPathSum(root.right, currentSum - root.val)

        
        return traverseEachNode(root, target)
            