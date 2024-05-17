'''
  idea: tranpose the matrix then reverse all rows of it.
  you can use arr.reverse() built in method
  time is O(n^2)
  memory is O(1)
'''

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #lets tranpose the matrix
        #then for each row lets reverse it
        def reverse(row):
            l, r = 0, len(row) - 1
            while l < r:
                row[l], row[r] = row[r], row[l]
                l += 1
                r -= 1
            return row
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            row = reverse(row)