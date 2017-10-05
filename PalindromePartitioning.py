# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(word):
            return word == word[::-1]
        def partitionHelper(s, cur, curStartPoint, result = []):
            if(curStartPoint == len(s)):
                result.append(cur)
                return result
            for i in range(curStartPoint + 1, len(s) + 1):
                if(isPalindrome(s[curStartPoint:i])):
                    partitionHelper(s, cur + [s[curStartPoint:i]], i, result)
            return result
        return partitionHelper(s, [], 0)