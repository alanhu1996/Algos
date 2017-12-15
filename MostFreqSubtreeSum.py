# Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def outputAllSumFreqTable(root, freqTable={}):
            if not root:
                return freqTable
            sumAtNode = findSubSumAtNode(root)
            freqTable[sumAtNode] = 1 if sumAtNode not in freqTable else freqTable[sumAtNode] + 1
            outputAllSumFreqTable(root.left, freqTable)
            outputAllSumFreqTable(root.right, freqTable)
            return freqTable
        def findSubSumAtNode(root):
            if not root:
                return 0
            return root.val + findSubSumAtNode(root.left) + findSubSumAtNode(root.right)
        resultTable = outputAllSumFreqTable(root)

        # Find the max value.
        maxFreq = max(resultTable.values()) if len(resultTable.keys()) > 0 else 0
        
        return [key for key in resultTable if resultTable[key] == maxFreq]