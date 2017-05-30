# Reversing a singly linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oldNext = None
        newNext = None
        while(head != None):
            oldNext = head.next
            head.next = newNext
            newNext = head
            head = oldNext
        
        return newNext
          
            
            