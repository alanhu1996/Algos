# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).


import Queue
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Check for root case.
        if(not root):
            return []
        q = Queue.Queue()
        q.put(root)
        
        def levelOrderHelper(root, result = []):
            while(not q.empty()):
                qSize = q.qsize()
                levelResult = []
                for i in range(qSize):
                    item = q.get()
                    levelResult.append(item.val)
                    if(item.left):
                        q.put(item.left)
                    if(item.right):
                        q.put(item.right)
                result.append(levelResult)
            return result
                    
                
                
        return levelOrderHelper(root)