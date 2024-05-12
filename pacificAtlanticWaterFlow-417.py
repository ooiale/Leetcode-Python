'''
  run DFS through every corner of the grid (aka starting at the ocean) and
  climb up the grid mapping every (i, j) that can be reached by the ocean.
  at the end we take the intersection of all coordinates (i, j) that are 
  in the atlantic set and the pacific set.
  Time is O(m * n) 
  Memory is O(m + n)
'''

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #pacific ocean => (i, j), i = 0 or j = 0
        #atlantic ocean => (i, j), i = len(heights), j = len(heights[0])
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(i, j, ocean): #dfs coming from the ocean:
            if j < COLS - 1 and (i, j + 1) not in ocean and heights[i][j+1] >= heights[i][j]:
                ocean.add((i, j + 1))
                dfs(i, j+1, ocean)
            if i < ROWS - 1 and (i + 1, j) not in ocean and heights[i + 1][j] >= heights[i][j]:
                ocean.add((i + 1, j))
                dfs(i + 1, j, ocean)
            if j > 0 and (i, j - 1) not in ocean and heights[i][j-1] >= heights[i][j]:
                ocean.add((i, j - 1))
                dfs(i, j - 1, ocean)
            if i > 0 and (i - 1, j) not in ocean and heights[i - 1][j] >= heights[i][j]:
                ocean.add((i - 1, j))
                dfs(i - 1, j, ocean)

        for i in range(ROWS):
            pacific.add((i, 0))
            dfs(i, 0, pacific)
            atlantic.add((i, COLS - 1))
            dfs(i, COLS - 1, atlantic)
        for j in range(COLS):
            pacific.add((0, j))
            dfs(0, j, pacific)
            atlantic.add((ROWS - 1, j))
            dfs(ROWS - 1, j, atlantic)

        return(list(atlantic.intersection(pacific)))
 
            