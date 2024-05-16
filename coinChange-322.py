'''
  compute the minimum number of coins to reach every amount <= given amount.
  starting from the base case: 0 coins for 0 amount, we can start computing
  the number needed of coins to achieve every amount. 
  time is O(amount * coins)
  memory is O(amount)
'''

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coinsByAmount = [amount + 1] * (amount + 1)
        coinsByAmount[0] = 0
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    coinsByAmount[a] = min(coinsByAmount[a], coinsByAmount[a - coin] + 1)
        if coinsByAmount[amount] == amount + 1:
            return -1
        return coinsByAmount[amount]