'''
  set two pointers that are always 1 house and 2 houses before
  the current value at the array.
  at this point in time, you could either have robbed the amount you made
  from rob1 and rob the current house or just rob everything up to rob2.
  select the best decision and move to the next house for the next decision.
  Time is O(n)
  memory is O(1)
'''

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        #[0, 1, 2, ..., n]
        #[rob1, rob2, i+1, ..., n]
        #update the value at the array by the max amount you could have robbed so far
        rob1, rob2 = 0, 0
        for n in nums:
            n = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = n
        return rob2