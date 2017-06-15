class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in xrange(1, n + 1):
            node = ""
            if(i % 3 == 0):
                node += "Fizz"
            if(i % 5 == 0):
                node += "Buzz"
            if(node == ""):
                node = str(i)
            result.append(node)
            
        return result