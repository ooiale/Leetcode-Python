'''
  perform a simultaneous BFS at every rotten orange. after each BFS iteration,
  increase time by 1. An edge case arises at the last BFS iteration, since it
  will not rot any fruits. so if your time is greater than 0, we should decrement it by 1 because the last iteration did not rot any fruits.
  this can be easily avoided and this code also could have a lot of 
  refactoring. 
  time is O(m*n)
'''

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        def rotNeighbor(i, j):
            if i >= 0 and i < ROWS and j >= 0 and j < COLS:
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    return True
        #lets find all rotting fruits 
        queue = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        #now we run a bfs on all rotting fruits and compute the time
        #it takes to rot all fruits possible
        time = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if rotNeighbor(r + 1, c):
                    queue.append((r + 1, c))
                    fresh -= 1
                if rotNeighbor(r, c + 1):
                    queue.append((r, c + 1))
                    fresh -= 1
                if rotNeighbor(r - 1, c):
                    queue.append((r - 1, c))
                    fresh -= 1
                if rotNeighbor(r, c - 1):
                    queue.append((r, c - 1))
                    fresh -= 1
            time += 1
        
        if fresh > 0:
            return - 1
        return time - 1 if time > 0 else time

        

        