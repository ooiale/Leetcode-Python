'''
  just computing each row of the triangle but using only 2 rows at a time.
  the current one and the previous one
'''

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row1 = [1]
        for i in range(1, rowIndex + 1):
            row2 = [1] * (i + 1)
            for j in range(1, i):
                row2[j] = row1[j - 1] + row1[j]
            row1 = row2
        return row1
