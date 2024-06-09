'''
  use DP here. we could do a bottom up or top bottom. it works the same.
  so on a bottom up we know that the last row already contain the minimum
  falling path sum.
  now on the row above it, for each element, the minimum falling path sum
  is the sum of the element itself plus the smallest element below it.
  compute this for all rows and return the smallest value in the first row
  time is O(n^2)
  memory is O(1)
'''

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        for row in range(ROWS - 2, -1, -1):
            for col in range(COLS):
                cur = matrix[row][col]
                fallLeft = matrix[row + 1][col - 1] if col - 1 >= 0 else float("inf")
                fallMiddle = matrix[row + 1][col]
                fallRight = matrix[row + 1][col + 1] if col + 1 < COLS else float('inf')
                minFall = min(fallLeft, fallMiddle, fallRight)
                matrix[row][col] = minFall + cur
        return min(matrix[0])