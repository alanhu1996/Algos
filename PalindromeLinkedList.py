# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        # Edge case.
        if head == None or head.next == None:
            return True
        def reverseList(start):
            prev = None
            oldNext = None
            current = start
            while current != None:
                oldNext = current.next
                current.next = prev
                prev = current
                current = oldNext
            return prev
        while fast and fast.next != None:
            if fast != slow:
                slow = slow.next
            fast = fast.next.next
        firstHalfPointer = head
        # Remove link from first section to the second section.
        startOfSecondHalf = slow.next
        slow.next = None
        secondHalfPointer = reverseList(startOfSecondHalf)

        while firstHalfPointer != None and secondHalfPointer != None:
            if firstHalfPointer.val != secondHalfPointer.val:
                return False
            firstHalfPointer = firstHalfPointer.next
            secondHalfPointer = secondHalfPointer.next
        return True