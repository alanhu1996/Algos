# Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


import Queue
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = Queue.Queue()
        q.put({'value': root, 'id': 1})
        maxWidth = 0
        
        while not q.empty():
            currentSize = q.qsize()
            mostLeft = None
            for i in range(currentSize):
                node = q.get()
                if not mostLeft and node:
                    mostLeft = node
                maxWidth = max(maxWidth, node['id'] - mostLeft['id'] + 1)

                if(node['value'].left):
                    q.put({'value': node['value'].left, 'id': node['id'] * 2})
                if(node['value'].right):
                    q.put({'value': node['value'].right, 'id': node['id'] * 2 + 1})
        return maxWidth
            