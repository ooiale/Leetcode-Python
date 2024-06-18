'''
  we can see this as a minimum path problem in a graph which we can solve
  using djistra algorithm. 
  so we will run a BFS in the grid with a minHeap instead of a queue.
  there are 2 possible ways of keeping track of the elevation.
  we could always pass to the minHeap the value max(curElevation, nextElevation)
  or like is done here, we just pass to the minHeap the value of the grid element itself but keep track in another variable the maxElevation seen so far.
  time is O(E log(E)) where E is the number of edges or
  O(n^2 log(n)) with n being the number of nodes
'''

import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def inBounds(idx, n):
            return idx >= 0 and idx < n

        n = len(grid)
        elevation = grid[0][0]
        minHeap = [[elevation, 0, 0]]
        visited = set()
        while minHeap:
            newElevation, i, j = heapq.heappop(minHeap)

            #base case: already visited
            if (i,j) in visited:
                continue
            
            visited.add((i, j))
            elevation = max(newElevation, elevation)
            if i == n - 1 and j == n - 1:
                return elevation

            if inBounds(i + 1 ,n):
                heapq.heappush(minHeap, [grid[i+1][j], i+1, j])
            if inBounds(i - 1 ,n):
                heapq.heappush(minHeap, [grid[i - 1][j], i - 1, j])
            if inBounds(j + 1 ,n):
                heapq.heappush(minHeap, [grid[i][j + 1], i, j + 1])
            if inBounds(j - 1,n):
                heapq.heappush(minHeap, [grid[i][j - 1], i, j - 1])
        

