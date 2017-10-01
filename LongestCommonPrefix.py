class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longestPrefix = ''
        i = 0
        if(len(strs) == 0):
            return ''
        while(True):
            isMatch = True
            if i >= len(strs[0]):
                return longestPrefix
            comp = strs[0][i]
            for word in strs:
                if i >= len(word):
                    return longestPrefix
                if comp != word[i]:
                    isMatch = False
                    break
            longestPrefix = longestPrefix + comp if isMatch else longestPrefix
            i += 1
            
        return longestPrefix


s = Solution()
print(s.longestCommonPrefix(['bvdc']))