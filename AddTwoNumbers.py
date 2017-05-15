# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carryOver = 0
        p1 = l1
        p2 = l2
        head = result = ListNode(0)

        while p1 or p2 or carryOver:
            value1 = 0
            value2 = 0
            if p1:
                value1 = p1.val
                p1 = p1.next
            if p2: 
                value2 = p2.val
                p2 = p2.next
            result.next = ListNode(divmod(value1 + value2 + carryOver, 10)[1])
            carryOver = value1 + value2 + carryOver >= 10
            result = result.next
        return head.next