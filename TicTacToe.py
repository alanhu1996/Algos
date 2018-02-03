# Design a Tic-tac-toe game that is played between two players on a n x n grid.

# You may assume the following rules:

# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves is allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.


class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.boardLength = n
        self.rowCounters = [0] * n
        self.colCounters = [0] * n
        self.diagonal = 0
        self.reverseDiagonal = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        addVal = 1 if player == 1 else -1
        self.rowCounters[row] += addVal
        self.colCounters[col] += addVal
        if row == col:
            self.diagonal += addVal
        if col == self.boardLength - row - 1:
            self.reverseDiagonal += addVal

        gameIsWon = self.boardLength == abs(self.rowCounters[row]) or self.boardLength == abs(self.colCounters[col]) or abs(self.diagonal) == self.boardLength or abs(self.reverseDiagonal) == self.boardLength
        
        if gameIsWon:
            return player
        else:
            return 0
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)