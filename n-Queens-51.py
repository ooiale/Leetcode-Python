'''
  for each row we will try to place a queen in every single col
  before placing the queen just check if that col is free, and if both
  diagonal are also free. 
  To keep track of the used cols and diags we will use 3 Set()
  cols set is simple to understand
  for both diagonals, notice that either the sum or the difference
  remains constant.
  to keep drawing the boards, initialize a matrix board to easily
  place the "Q" when possible but since we want the boards
  as strings, we just join all the rows from the board matrix into
  the string.
  time is O(n^2)
'''

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #given n queens,
        #try to place them in a n x n board
        #go row by row placing a queen anywhere possible
        #1 queen per row, keep track of the cols
        #to track diagonals, see that either (r-c) or (r + c)
        #are constant throughout the diagonal that goes tl - br and bl- tr
        cols, negDiag, posDiag = set(), set(), set()
        output = []
        board = [["."] * n for _ in range(n)]
        def backtrack(row):
            if row == n:
                output.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col not in cols and (row - col) not in negDiag and (row + col) not in posDiag:
                    cols.add(col)
                    negDiag.add(row-col)
                    posDiag.add(row+col)
                    board[row][col] = "Q"

                    backtrack(row + 1)

                    cols.remove(col)
                    negDiag.remove(row-col)
                    posDiag.remove(row+col)
                    board[row][col] = "."
                    
                    
        backtrack(0)
        return output