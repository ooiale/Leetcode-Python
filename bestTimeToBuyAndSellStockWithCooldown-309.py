'''
  at every element of the array we always have two choices:
  we either buy/sell or have a cooldown. to keep track whether we can 
  buy or sell we will have a bool var in the recursion function.
  in this case we end up making a binary tree with 2^n nodes. to
  optmize this we can use a cache to store the computed values to reduce
  to O(n). whenever we sell an item we are forced to take a cooldown so
  just move 2 index on the array.
  time is O(n)
'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #if we buy idx + 1
        #if we sell idx + 2 (aka forcing a cooldown on idx + 1)
        cache = {} #key = (idx, buying = Bool)

        def dfs(idx, buying): #buying is bool that indicates if we can buy on this day
            if idx >= len(prices):
                return 0
            if (idx, buying) in cache:
                return cache[(idx, buying)]
            
            #we can take a cooldown
            cooldownProfit = dfs(idx + 1, buying)
            if buying: #we can buy
                buyProfit = dfs(idx + 1, not buying) - prices[idx]
                cache[(idx, buying)] = max(cooldownProfit, buyProfit)
            else: #we can sell
                sellProfit = dfs(idx + 2, not buying) + prices[idx]
                cache[(idx, buying)] = max(cooldownProfit, sellProfit)
            
            return cache[(idx, buying)]
        return dfs(0, True)