# Given numRows, generate the first numRows of Pascal's triangle.
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = [[1]]
        for i in range(1, numRows):
            val = []
            for s in range(i + 1):
                appendVal = 1 if s - 1 < 0 or s >= len(result[-1]) else result[i - 1][s - 1] + result[i - 1][s]
                val.append(appendVal)
            result.append(val)
        return result