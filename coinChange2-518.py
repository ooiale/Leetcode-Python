'''
  this is a solution using backtracking with memoization (cache)
  for every coin we can always make two choices:
  1- pick the current coin (current idx) and move to the next choice
  2- don't pick the current coin and move to another coin
  and by caching the combination of ways to achieve the desired amount
  based on the curAmount and the idx we can reduce the time complexity
  it is possible to use a 2D DP cache as well.
  
'''

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = {}
        
        def dfs(curAmount, idx):
            if curAmount > amount or idx >= len(coins):
                return 0
            if curAmount == amount:
                return 1
            if (curAmount, idx) in cache:
                return cache[(curAmount, idx)]
            
            cache[(curAmount, idx)] = dfs(curAmount + coins[idx], idx) + dfs(curAmount, idx + 1)
            return cache[(curAmount, idx)]

        return dfs(0, 0)
