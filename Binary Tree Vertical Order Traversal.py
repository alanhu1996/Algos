import Queue
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodeq = Queue.Queue()
        colQ = Queue.Queue()
        if not root:
            return []
        nodeq.put(root)
        colDict = collections.defaultdict(list)
        colQ.put(0)
        minCol = 0
        maxCol = 0
        while not nodeq.empty():
            for i in xrange(nodeq.qsize()):
                node = nodeq.get()
                currentLevel = colQ.get()
                minCol = min(minCol, currentLevel)
                maxCol = max(maxCol, currentLevel)
                if node.left:
                    nodeq.put(node.left)
                    colQ.put(currentLevel - 1)
                if node.right:
                    nodeq.put(node.right)
                    colQ.put(currentLevel + 1)
                colDict[currentLevel].append(node.val)
        
        result = []
        for i in xrange(minCol, maxCol + 1):
            result.append(colDict[i])
        return result
        
                
            