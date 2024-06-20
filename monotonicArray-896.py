'''
  start two booleans that will tell if the sequence is increasing or decreasing.
  if we find that two consecutive elements are increasing then dec = false
  if two consecutive elements are decreasing then inc = false.
  at the end return inc or dec
  time is O(n)
'''

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc, dec = True, True

        i = 0
        while (inc or dec) and i < len(nums) - 1:
            if nums[i] < nums[i + 1]:
                inc = False
            elif nums[i] > nums[i + 1]:
                dec = False
            i += 1
        return inc or dec