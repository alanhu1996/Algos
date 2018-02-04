# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

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
        stack1 = []
        stack2 = []
        l1Current = l1
        l2Current = l2
        while l1Current:
            stack1.append(l1Current)
            l1Current = l1Current.next
        while l2Current:
            stack2.append(l2Current)
            l2Current = l2Current.next
            
        length1 = len(stack1)
        length2 = len(stack2)
        
        currentNode = ListNode(0)
        while len(stack1) > 0 or len(stack2) > 0:
            sumVal = currentNode.val

            if len(stack1) > 0: 
                sumVal += stack1.pop().val
            if len(stack2) > 0:
                sumVal += stack2.pop().val
                
            currentNode.val = sumVal % 10
            carry = sumVal / 10
            nextNode = ListNode(carry)
            nextNode.next = currentNode
            currentNode = nextNode
        
        return currentNode if currentNode.val != 0 else currentNode.next
            
            
        