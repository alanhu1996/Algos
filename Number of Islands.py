# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        isVisited = [[False for s in xrange(len(grid[0]))] for i in xrange(len(grid))]
        def dfsHelper(row, col, grid, isVisited):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0' or isVisited[row][col]:
                return False
            
            isVisited[row][col] = True
            dfsHelper(row, col - 1, grid, isVisited)
            dfsHelper(row, col + 1, grid, isVisited)
            dfsHelper(row - 1, col, grid, isVisited)
            dfsHelper(row + 1, col, grid, isVisited)
            
        totalIslands = 0
        for row in xrange(len(grid)):
            for col in xrange(len(grid[0])):
                if not isVisited[row][col] and grid[row][col] == '1':
                    dfsHelper(row, col, grid, isVisited)
                    totalIslands += 1
        return totalIslands
                    