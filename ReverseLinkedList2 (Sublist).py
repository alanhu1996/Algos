# Reverse a linked list from position m to n. Do it in-place and in one-pass.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        # This function returns to the head of the reversed sub list. It also connects the tail of the reversed list to the second half of the entire list.
        def reverse(steps, startPoint):
            begin = startPoint
            prev = None
            for i in range(steps + 1):
                oldNext = begin.next
                begin.next = prev
                prev = begin
                begin = oldNext
                
            # begin is now at the beginning of the part of the linked list right after the reversed sub list.
            # We now connect the tail of the reversed list to this node.
            startPoint.next = begin
            # Prev will be the first element of the reversed sub list.
            return prev
            
        dummy = ListNode(0)
        dummy.next = head
        
        startPoint = head
        startPrev = None
        
        # Find start point.
        for i in range(m - 1):
            startPoint = startPoint.next     
            if startPrev:
                startPrev = startPrev.next
            else:
                startPrev = head

        # Apply reverse function to the startpoint for n - m nodes.
        if startPrev:
            startPrev.next = reverse(n - m, startPoint)
        else:
            dummy.next = reverse(n - m, startPoint)

        return dummy.next