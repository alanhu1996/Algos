# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of 
# the first two lists.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = newList = ListNode(0)
        while(l1 != None and l2 != None):
            if(l1.val < l2.val):
                newList.next = ListNode(l1.val)
                newList = newList.next
                l1 = l1.next
            else:
                newList.next = ListNode(l2.val)
                newList = newList.next
                l2 = l2.next
        endList = l1 if l1 != None else l2
        newList.next = endList
    
        return head.next