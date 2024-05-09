'''
  the rotated sorted array contains two sorted arrays in it.
  use binary search to find where the middle is at.
  once located what side m is, check where the target can be found:
  at left of m or at right of m. move the pointers accordingly
  time is O(log(n))
'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (l + r)//2
            if target == nums[m]:
                return m
            
            #m is on left side
            if nums[m] >= nums[l]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
            #m is on right side
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                elif target > nums[m]:
                    l = m + 1
        return - 1
