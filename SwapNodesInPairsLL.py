# Given a linked list, swap every two adjacent nodes and return its head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def helper(head):
            if not head or not head.next:
                return head
            temp = head.next
            head.next = helper(head.next.next)
            temp.next = head
            return temp
            
            
        return helper(head)
            