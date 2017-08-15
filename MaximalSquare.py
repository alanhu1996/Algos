# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        # Edge case.
        if matrix == []:
            return 0
        height = len(matrix)
        width = len(matrix[0])
        
        sumMatrix = []
        maxValue = 0
        sumVal = 0
        for row in range(height):
            rowData = []
            sumMatrix.append(rowData)
            for col in range(width):
                if (row >= 1 and col >= 1):
                    sumVal = min(int(sumMatrix[row][col - 1]), int(sumMatrix[row - 1][col - 1]), int(sumMatrix[row - 1][col])) + 1 if matrix[row][col] != "0" else int(matrix[row][col])
                else:
                    sumVal = int(matrix[row][col])

                rowData.append(sumVal)
                maxValue = sumVal if maxValue < sumVal else maxValue

        
        return pow(maxValue, 2)