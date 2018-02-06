# Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

# The input string does not contain leading or trailing spaces and the words are always separated by a single space.

# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

# Could you do it in-place without allocating extra space?



class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """

        def reverse(start, end, strList):
            while start < end:
                temp = strList[start]
                strList[start] = strList[end]
                strList[end] = temp
                start += 1
                end -= 1
            
        
        
        reverse(0, len(str) - 1, str)
        start = 0
        for i in xrange(start, len(str) + 1):
            if i == len(str) or str[i] == " ":
                reverse(start, i - 1, str)
                start = i + 1
