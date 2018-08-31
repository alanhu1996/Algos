# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
import Queue 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        result = []
        q = Queue.Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            if not node:
                result.append('None')
            else:
                result.append(str(node.val))
            
                q.put(node.left)
                q.put(node.right)
            
        # string join is more efficient than multiple concatenations
        return ','.join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        dataList = data.split(',')
        q = Queue.Queue()
        root = TreeNode(dataList[0])
        q.put(root)
        for i in range(1, len(dataList), 2):
            node = q.get()
            if dataList[i] != "None":
                node.left = TreeNode(dataList[i])
                q.put(node.left)
          
            if dataList[i + 1] != "None":
                node.right = TreeNode(dataList[i + 1])
                q.put(node.right)
          
        return root
            
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))