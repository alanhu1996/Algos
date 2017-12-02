import Queue
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q = Queue.Queue()
        q.put(root)
        total = 0   
        result = []
        while not q.empty():
            currentLevelAmount = q.qsize()
            for i in range(currentLevelAmount):
                currentNode = q.get()
                total += currentNode.val
                if currentNode.left:
                    q.put(currentNode.left)
                if currentNode.right:
                    q.put(currentNode.right)
            levelAvg = float(total) / currentLevelAmount
            result.append(levelAvg)
            total = 0
        return result