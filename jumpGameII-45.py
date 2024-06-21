'''
  we always want to jump to the index/element that will give us the most
  coverage of the array. we have this check of maxJumpIdx >= end for the edge
  case we can complete the game on the first round
  time is O(n)
'''

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = 0
        end = len(nums) - 1

        while l < end:
            maxJump = nums[l]
            maxJumpIdx = l + maxJump
            if maxJumpIdx >= end:
                return jumps + 1
            for i in range(nums[l]):
                if l + i + 1 < len(nums):
                    if nums[l + i + 1] + i + 1 > maxJump:
                        maxJump = nums[l + i + 1] + i + 1
                        maxJumpIdx = l + i + 1
            jumps += 1
            l = maxJumpIdx
        return jumps

