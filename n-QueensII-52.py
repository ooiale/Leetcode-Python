'''
  literally same code from n-Queens-51.py but instead of creating the board, we just
  increment a global variable output by 1 to access this variable within the function, we could either initialize the variable as an array or write nonlocal output in the backtracking function 
  time is O(n^2)
'''

class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, negDiag, posDiag = set(), set(), set()
        output = 0
        def backtrack(row):
            if row == n:
                nonlocal output
                output += 1
                return 
            for col in range(n):
                if col not in cols and (row - col) not in negDiag and (row + col) not in posDiag:
                    cols.add(col)
                    negDiag.add(row - col)
                    posDiag.add(row + col)

                    backtrack(row + 1)

                    cols.remove(col)
                    negDiag.remove(row - col)
                    posDiag.remove(row + col)
        backtrack(0)
        return output