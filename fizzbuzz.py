# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
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