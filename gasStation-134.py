'''
  very elegant problem:
  so first step is to check if there is a solution. (first line)
  now, we know that there is a solution.
  the idea will be to compute the postfix of the dif array 
  where dif is gas - cost. and because THERE is a solution, this solution is
  located at the max of the postfix matrix.
  what this postfix arr is telling us is how much fuel the car will have at the
  end of the array if it started at the index i. If we can maximize this value
  we guarantee that the car will be able to complete the loop.
  time is O(n)
'''

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        i = len(gas) - 1
        maxSoFar, maxIdx, aux = 0, 0, 0
        while i > 0:
            aux += gas[i] - cost[i]
            if aux > maxSoFar:
                maxSoFar = aux
                maxIdx = i
            i -= 1
        return maxIdx