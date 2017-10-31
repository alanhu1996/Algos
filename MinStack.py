# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.minNum = sys.maxint

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.minNum = x if x < self.minNum else self.minNum
        self.data.append((x, self.minNum))
        
    def pop(self):
        """
        :rtype: void
        """
        del self.data[len(self.data) - 1]
        self.minNum = sys.maxint if len(self.data) == 0 else self.data[len(self.data) - 1][1]
        
        

    def top(self):
        """
        :rtype: int
        """
        return self.data[len(self.data) - 1][0] if len(self.data) > 0 else None
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minNum if len(self.data) > 0 else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()