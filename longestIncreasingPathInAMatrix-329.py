'''
  do a dfs with a cache to keep track of the max path at every
  index (i, j)
  time is O(m * n)
'''

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {} #(i, j) => max ways

        def dfs(i, j, prevVal):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] <= prevVal:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            curValue = matrix[i][j]
            r = dfs(i + 1, j, curValue)
            d = dfs(i, j + 1, curValue)
            l = dfs(i - 1, j, curValue)
            u = dfs(i, j - 1, curValue)
            cache[(i, j)] = max(r, d, l, u) + 1
            return cache[(i, j)]
        
        res = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res , dfs(i, j, -1))
        print(cache)
        return res