'''
  start with the left and right pointer trick. this way we ensure the maximum
  area as far as width is concerned. now if we want to possibly increase the area we need to slide the pointer at the smaller height. always compare the new area with the largest found.
  time is O(n)
  memory is O(1)
'''

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        largest = 0
        while l < r:
            area  = (r - l) * (min(height[l], height[r]))
            largest = max(largest, area)
            if height[l] < height[r]:
                l += 1
            else:
                r-= 1
        return largest
