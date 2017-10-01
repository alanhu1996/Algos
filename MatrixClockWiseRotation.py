# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).

# Rotation must be in-place.

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def swap2D(i, j):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
        def swap1D(upper, lower, col):
            temp = matrix[upper][col]
            matrix[upper][col] = matrix[lower][col]    
            matrix[lower][col] = temp
        for upper in range(len(matrix) / 2):
            lower = len(matrix) - 1 - upper
            for col in range(len(matrix[upper])):
                swap1D(upper, lower, col)
        
        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix)):
                swap2D(row, col)
        print(matrix)