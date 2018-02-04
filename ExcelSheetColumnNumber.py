# Related to question Excel Sheet Column Title

# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 

class Solution(object):
    def titleToNumberRecursive(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        # It's similar to int except this is base 26.
        rightMostCharacterNumVal = (ord(s[-1]) - ord('A') + 1)
        return self.titleToNumber(s[0:len(s) - 1]) * 26 + rightMostCharacterNumVal
    
    def titleToNumberReduce(self, s):
        return reduce(lambda val, acc: val * 26 + acc, [ord(i) - ord('A') + 1 for i in list(s)])
    
    def titleToNumber(self, s):
        return self.titleToNumberReduce(s)