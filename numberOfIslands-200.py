'''
  make a loop through every cell of the grid. but once you find a 1,
  we apply a recursive DFS (alternatively we could use a queue and do a iterative BFS or a stack and apply iterative DFS). This DFS will visit
  every adjacent cell to the initial 1 and visit all of them. after everything is visited we are safe to increment islands += 1. To keep track of the cells visited and not visit it again, we store the coords (x, y) in a set.
  Time complexity: O(n^2)
'''

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def search (r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            if (r, c) in visited:
                return
            visited.add((r, c))
            if grid[r][c] == "1":
                search(r + 1, c)
                search(r, c + 1)
                search(r - 1, c)
                search(r, c - 1)
            return
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j] == "1":
                    search(i, j)
                    islands += 1

        return islands