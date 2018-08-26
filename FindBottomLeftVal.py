import Queue as queue
# Definition for a binary tree node.
# Given a binary tree, find the leftmost value in the last row of the tree.

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
        # BFS solution
        def bfs():
            q = queue.Queue()

            q.put(root)
            leftMostNode = None
            while not q.empty():
                for i in range(q.qsize()):
                    node = q.get()
                    if i == 0:
                        leftMostNode = node
                    if node.left:
                        q.put(node.left)
                    if node.right:
                        q.put(node.right)
            return leftMostNode.val
        def dfs(root, currentDepth, leftMostNode = [-1, -1]):
            if not root:
                return None
            # Check for depth
            if currentDepth > leftMostNode[1]:
                leftMostNode[1] = currentDepth
                leftMostNode[0] = root.val
            dfs(root.left, currentDepth + 1, leftMostNode)
            dfs(root.right, currentDepth + 1)
            return leftMostNode[0]
            
            
        return dfs(root, 0)