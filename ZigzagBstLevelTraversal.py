
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        l = []
        l.append(root)
        level = 0
        result = []
        size = 1
        while(len(l) > 0):
            subRes = []
            for i in range(size):
                # We always want to insert in this order for the list [root.left, root.right].
                # Doesn't matter if we are appending to the back or inserting to the front of the list,
                # the left first then right node order must be maintained.
                if len(result) % 2 == 0:
                    node = l.pop(0)
                    if node.left:
                        l.append(node.left)
                    if node.right:
                        l.append(node.right)
                else:
                    node = l.pop(-1)
                    if node.right:
                        l.insert(0, node.right)
                    if node.left:
                        l.insert(0, node.left)
                subRes.append(node.val)

            size = len(l)
            level += 1
            result.append(subRes)
        return result