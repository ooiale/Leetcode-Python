'''
  this is a backtracking solution for this problem that runs in O(n) with memory O(n)
  the decision tree is basically: we either skip or (buy/sell). so by using a cache we can reduce the time complexity from O(2^n) to O(n)
  but there is a more simple solution that basically involves running through the array and ask arr[i] > arr[i - 1]? if so we buy on day i - 1 and sell on day i 
  otherwise we don't buy on i - 1 which grant us a memory complexity of O(1):
  class Solution:
      def maxProfit(self, prices: List[int]) -> int:
          profit = 0
          for i in range(1, len(prices)):
              if prices[i] > prices[i - 1]:
                  profit += prices[i] - prices[i - 1]
          return profit
  this is very tricky because being able to buy and sell on the same day or not, 
  does not affect the final result 
'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {} # day, bought => profit
        
        def dfs(day, bought): # bought = False => we can buy, True => must sell
            if day >= len(prices):
                return 0
            
            if (day, bought) in cache:
                return cache[(day, bought)]
            
            # Skip this day
            skip = dfs(day + 1, bought)
            
            if bought:
                # We must sell or skip
                sell = dfs(day + 1, not bought) + prices[day]
                cache[(day, bought)] = max(sell, skip)
            else:
                # We must buy or skip
                buy = dfs(day + 1, not bought) - prices[day]
                cache[(day, bought)] = max(buy, skip)
            
            return cache[(day, bought)]
        
        return dfs(0, False)