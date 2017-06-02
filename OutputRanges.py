# Given a sorted integer array without duplicates, return the summary of its ranges.

# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        
        """
        result = []
        for i in nums:
            if(not result or i > result[-1][-1] + 1):
                result.append([])
            # Automatically inputs the range.
            result[-1][1:] = [i]
        
        # Outputting the range.
        return list("->".join(map(str, n)) for n in result)
        
                

