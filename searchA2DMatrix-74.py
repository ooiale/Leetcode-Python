'''
  since the matrix is fully ordered we can run a binary search to find
  the row the target is in. having found the row, run a binary search on that
  row to find the column of the target.
  time is O(logm + logn) = O(logmn)
'''

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #m tall, n large
        ROWS, COLS = len(matrix), len(matrix[0])
        
        #lets find the row:
        top, bottom = 0, ROWS - 1
        while top <= bottom:
            m = (top + bottom) // 2
            if matrix[m][-1] < target:
                top = m + 1
            elif matrix[m][0] > target:
                bottom = m - 1
            else:
                break
        if top > bottom:
            return False
        #lets find the column:
        row = (top + bottom) // 2
        l = 0
        r = COLS - 1
        while l <= r:
            m = (l + r)//2
            if matrix[row][m] == target:
                return True
            if target < matrix[row][m]:
                r = m - 1
            else:
                l = m + 1
        return False