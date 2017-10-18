# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Runtime: O(n) 
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        def getTail(head):
            start = head
            while(start != None and start.next != None):
                start = start.next
            return start
        def getMid(head, tail):
            slow = head
            fast = head
            while(fast != tail and fast != None and fast.next != tail and fast.next != None):
                slow = slow.next
                fast = fast.next.next
            return slow
        def getBeforeMid(head, target):
            start = head
            if(head == target):
                return None
            while(start != None and start.next != target):
                start = start.next
            return start
   
        def toBstHelper(head, tail):
            if head == None or tail == None or head.val > tail.val:
                return None
            mid = getMid(head, tail)

            root = TreeNode(mid.val)
            root.left = toBstHelper(head, getBeforeMid(head, mid))
            root.right = toBstHelper(mid.next, tail)
            return root
       
        return toBstHelper(head, getTail(head))