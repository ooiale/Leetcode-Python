'''
  using the sliding window technique, we start a left pointer at i = 0
  and a right pointer that will run through l + 1 to the end.
  compute the profit at each day searched. but if it would be possible to
  sell for less than what you bought aka negative profit we move the left pointer (indicates when we buy) to the right pointer.
  time is O(n) since l and r run through the array together.
  memory is O(1)
'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        for r in range (l + 1, len(prices)):
            sell = prices[r] - prices[l]
            profit = max(profit, sell)
            if sell < 0:
                l = r

        return profit