# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


class Solution(object):
    def generateParenthesis(self, n):
        def generate(leftNum, rightNum, permutation, result = []):
            if(leftNum):
                generate(leftNum - 1, rightNum, permutation + "(", result)
            if(leftNum < rightNum):
                generate(leftNum, rightNum - 1, permutation + ")", result)
            if(rightNum == 0):
                result.append(permutation)
            return result
        """
        :type n: int
        :rtype: List[str]
        """
        return generate(n, n, "")