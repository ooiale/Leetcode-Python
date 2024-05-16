'''
  compute backwards the minimum cost to go from that step until the end.
  all we need is the cost of the above step and the next one. Start them with 0
  so we don't need to treat the last 2 steps as edge cases.
  time is O(n)
  storage is O(1)
'''

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        next, nextnext = 0, 0
        for i in range(len(cost) - 1, -1, -1):
            next, nextnext = min(cost[i] + next, cost[i] + nextnext), next
        return min(next, nextnext)