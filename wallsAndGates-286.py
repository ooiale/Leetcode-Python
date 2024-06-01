'''
  we will get the position of each treasure chest and run a BFS on all of them.
  all adjacents tiles to it are dist 1 from a treasure, and the adjacents to these
  are dist 2 and so on... a queue is a good way to implement a bfs
  time is O(m*n)
'''

from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def addRoom(i, j):
            if (i < 0 or i >= ROWS or j < 0 or j >= COLS 
                or grid[i][j] == -1 or (i, j) in visited):
                return
            queue.append((i, j))
            
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        
        dist = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                grid[i][j] = min(grid[i][j], dist)
                visited.add((i, j))
                addRoom(i + 1, j)
                addRoom(i, j + 1)
                addRoom(i - 1, j)
                addRoom(i, j - 1)

            dist += 1
        return grid
                    
