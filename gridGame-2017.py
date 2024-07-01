'''
  lets create a [ [postfix], [prefix]] array. basically what this array will tell us is:
  if robot 1 moves to the bottom row at index i, how many points did he miss in row 0 (aka postfix sum at index i, row 0) and how many points did he miss in row 1 (aka prefix sum at index i, row 1). the idea of the algorithm is to leave the smallest value
  for robot 2. but remember that robot2 will always pick the biggest value that robot 1 
  leaves to him.
  time is O(n)
  memory is O(n)
'''

from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        #[11 9 4]
        #[7  6 1]
        WIDTH, HEIGHT = len(grid[0]), len(grid)
        postfix = [[0] * WIDTH for _ in range(HEIGHT)]
        
        total1 = grid[0][-1]
        total2 = grid[1][0]

        for j in range(1, WIDTH):
            postfix[0][-1 - j] = total1
            total1 += grid[0][-1 - j]
            postfix[1][j] = total2
            total2 += grid[1][j]
        
        res = float("inf")
        for i in range(len(grid[0])):
            points2 = max(postfix[0][i], postfix[1][i])
            res = min(res, points2)
        return res
        
        
