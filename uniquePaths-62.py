'''
  this is a combinatory problem which can be solved in O(1) with math
  below is a dynamic programming approach.
  we know that if we are on the bottom row or at the right most cells,
  there is only 1 path to reach the finish.
  and say, we are on cell [i][j], we know that the possible ways to reach the line from here are the number of ways in [i+1][j] + [j + 1][i] aka
  right and below cells.
  since we only care about the row below, we don't need to store the entire grid
  with all possible combinations. we can just store the row below the current one
  speed is O(m * n)
  memory is O(n)
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = row[j] + newRow[j + 1]
            row = newRow
        return row[0]