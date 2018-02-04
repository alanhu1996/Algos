# Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        totalShips = 0
        # All we need to count is the top left part of each ship. Thus, the left and up parts cannot be X.
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.' or (col > 0 and board[row][col - 1] == 'X') or (row > 0 and board[row - 1][col] == 'X'):
                    continue
                totalShips += 1
        return totalShips