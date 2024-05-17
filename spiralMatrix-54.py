'''
  this is veery confusing. the idea is to initialize 4 pointers. one at the top, right, left, bottom of the matrix. these will be the delimiters of the matrix for us to retrieve each cell. whenever we run through one of the line/column we update the respective pointer. you can initialize the right and bottom out of bounds which will simplify some things and change others. Draw the situation yourself for better understanding the algorithm.
  time is O(m x n)
'''

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        output = []
        while top <= bottom and left <= right:
            for r in range(left, right + 1):
                output.append(matrix[top][r])
            top += 1
            if top > bottom or left > right:
                break
            for d in range(top, bottom + 1):
                output.append(matrix[d][right])
            right -= 1
            for l in range(right, left - 1, -1):
                output.append(matrix[bottom][l])
            bottom -= 1
            if top > bottom or left > right:
                break
            for u in range(bottom, top - 1, -1):
                output.append(matrix[u][left])
            left += 1
        return output