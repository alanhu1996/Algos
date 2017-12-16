# Given a binary tree, find the leftmost value in the last row of the tree.

import Queue
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = Queue.Queue()
        
        q.put(root)
        # Using a right to left BFS, so the last element we encounter will be the left most element in the last level of the tree.
        while not q.empty():
            levelSize = q.qsize()
            for i in range(levelSize):
                node = q.get()
                if node.right:
                    q.put(node.right)
                if node.left:
                    q.put(node.left)

        return node.val
                
            