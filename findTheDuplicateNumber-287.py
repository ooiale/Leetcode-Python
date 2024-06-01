'''
  floyd's tortoise and hare algorithm:
  start 2 pointers slow and fast. find where they intercept in the cycle
  by moving slow by 1 and fast by 2
  start another slow pointer. the distance between this pointer and the previous slow (or fast) pointers to the start of the cycle is the same so, increment both by 1
  until they meet.
  time is O(n)
  memory is O(1)
'''

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return nums[0]
        s1 = 0
        s2 = 0
        f = 0
        while True:
            s2 = nums[s2]
            f = nums[nums[f]]
            if s2 == f:
                break
        while s1 != s2:
            s1 = nums[s1]
            s2 = nums[s2]
        return s1