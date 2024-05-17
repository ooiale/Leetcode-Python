'''
  Ill show two greedy solutions: the one I came up and the other from neetcode
  my idea was to always land on the square where you would be able to perform the longest leap. the leap is calculated as the longest jump you can make upon reaching this square + the jump you made to reach that one square. We will compute the value for every single cell reacheable from whatever cell we start.
  this solution is also time O(n) but makes some more operations than the next one

  Neetcodes approach was to start from the end, and make your way backwards pushing the goal to the start of the array whenever you find a cell that could reach the goal. time complexity is O(n):
  class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
'''

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = 0
        end = len(nums) - 1
        while l < end:
            maxJump = nums[l]
            maxJumpIdx = l + maxJump 
            if nums[l] == 0:
                return False
            for i in range(nums[l]):
                if l + 1 + i >= end:
                    return True
                if nums[l + 1 + i] + l + 1 + i >= maxJump:
                    maxJump = nums[l + 1 + i] + l + 1 + i
                    maxJumpIdx = l + 1 + i
            l = maxJumpIdx
        return True

            