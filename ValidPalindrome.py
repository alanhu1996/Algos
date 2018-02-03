class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftPointer = 0
        rightPointer = len(s) - 1
        while leftPointer < rightPointer:
            if(not s[leftPointer].isalpha() and not s[leftPointer].isdigit() and leftPointer < rightPointer):
                leftPointer += 1
            elif(not s[rightPointer].isalpha() and not s[rightPointer].isdigit() and leftPointer < rightPointer):
                rightPointer -= 1
            else:
                if s[leftPointer].lower() != s[rightPointer].lower():
                    return False
                leftPointer += 1
                rightPointer -= 1
        return True