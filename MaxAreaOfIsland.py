# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(row, col, grid, visited):
            if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or visited[row][col] or grid[row][col] == 0:
                return 0
            visited[row][col] = True
            upSum = dfs(row - 1, col, grid, visited)
            downSum = dfs(row + 1, col, grid, visited)
            rightSum = dfs(row, col + 1, grid, visited)
            leftSum = dfs(row, col - 1, grid, visited)
            total = downSum + rightSum + leftSum + upSum + 1
            return total
        total = 0
        visited = [[False for t in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j]:
                    total = max(total, dfs(i, j, grid, visited))
        return total
