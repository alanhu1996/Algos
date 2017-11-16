# Given a linked list, remove the nth node from the end of list and return its head.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = head
        slow = head
        fast = head
        # Make sure fast pointer is n nodes ahead of slow pointer.
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            pre = pre.next if slow != head else pre
            slow = slow.next
        if slow == head and fast == head:
            pre = None
        elif slow == head:
            head = pre.next
        else:
            pre.next = slow.next
        return head