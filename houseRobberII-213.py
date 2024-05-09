'''
  if the first and last house form a cycle, it means that
  it is not possible to rob both houses in one go.
  since each house exclude the possiblity of visiting the other,
  we will run the algorithm from house robber 1 on the array
  with the first house and not the last
  and compute using the array without the first house but including the last one. 
  then return the max value computed
  Time is O(n)
  memory is O(1)
'''

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def operation(houses):
            rob1 = 0
            rob2 = 0
            for n in houses:
                n = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = n
            return rob2
        return max(operation(nums[0:-1]), operation(nums[1::]))