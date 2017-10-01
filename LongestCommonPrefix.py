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
            if i >= len(strs[0]):
                return longestPrefix
            comp = strs[0][i]
            for word in strs:
                if i >= len(word) or comp != word[i]:
                    return longestPrefix
                    
            longestPrefix = longestPrefix + comp
            i += 1
            
        return longestPrefix


s = Solution()
print(s.longestCommonPrefix(["aca","cba"]))