'''
  sort the array so we can check intervals in ascending order.
  if the start of the interval i + 1 >= end of interval i then
  the intervals don't overlap
  else, we need to remove one of the two overlapping intervals.
  the choice here is to remove the interval that ends later since by doing so
  we may avoid overlapping intervals with the next one.
  time is O(n logn) for the sorting
'''

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = -float("inf")
        count = 0
        print(intervals)
        for i,j in intervals:
            if i < prevEnd:
                count += 1
                prevEnd = min(prevEnd, j)
            else:
                prevEnd = j
        return count
        