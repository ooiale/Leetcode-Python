'''
  do a dfs on each cell and if a land is found start doing a dfs on it 
  searching for more lands. 
  its possible to not use a hashSet() and instead just update the visited
  cell to 0. 
  time complexity is O(m * n) since we visit each cell once.
  memory is complexity of O(m * n) for the recurssion
'''

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        land = set()
        maxArea = 0
        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return 0
            if grid[i][j] == 0:
                return 0
            if (i, j) in land:
                return 0
            land.add((i, j))
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        
        for i in range(ROWS):
            for j in range(COLS):
                maxArea = max(maxArea, dfs(i, j))
        return maxArea
            
            