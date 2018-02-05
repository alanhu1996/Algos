# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        directionsIncs = [{"horizontal": 1, "vertical": 0}, 
                          {"horizontal": 0, "vertical": 1}, 
                          {"horizontal": -1, "vertical": 0}, 
                          {"horizontal": 0, "vertical": -1}]
        
        row = 0
        col = -1
        result = []
        directionsIndex = 0
        stepsArr = [len(matrix[0]), len(matrix) - 1]
        while stepsArr[directionsIndex % 2] > 0:
            for i in range(stepsArr[directionsIndex % 2]):
                row += directionsIncs[directionsIndex]["vertical"]
                col += directionsIncs[directionsIndex]["horizontal"]
                result.append(matrix[row][col])
            
            stepsArr[directionsIndex % 2] -= 1
            directionsIndex = (directionsIndex + 1) % len(directionsIncs)
        return result