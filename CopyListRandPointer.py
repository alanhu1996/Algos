# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        if not head:
            return head
        # First create a copy of the list without the random pointers.
        current = head

        while current != None:
            nextNode = current.next
            current.next = RandomListNode(current.label)
            current.next.next = nextNode
            current = nextNode
        
        # Setting the random pointers.
        current = head
        while current != None and current.next != None:
            # The next node is always the clone.
            current.next.random = current.random.next if current.random != None else None
            current = current.next.next
        
        # current = head
        # while current:
        #     print(current.label)
        #     current = current.next
        current = head
        newHead = head.next
        newCurrent = newHead
        # Extract cloned list.
        while newCurrent != None:
            originalNext = current.next.next 
            # Check to see if this is the last node.
            nextNode = newCurrent.next.next if newCurrent.next != None else None
            newCurrent.next = nextNode
            newCurrent = newCurrent.next
            # Restoring the orginal list.
            current.next = originalNext
            current = current.next
            
        return newHead

# Test code.
solution = Solution()
head = RandomListNode(0)
n1 = RandomListNode(1)
n2 = RandomListNode(2)
head.next = n1
n1.next = n2
head.random = n2
n1.random = head

clone = solution.copyRandomList(head)
current = clone
while current != None:
    print(current.label)
    current = current.next
