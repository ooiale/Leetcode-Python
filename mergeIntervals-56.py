'''
  sort the intervals so we can iterate in the ascending order
  of the intervals. 
  if we find intervals that overlap, iterate through all following intervals
  that remain overlapping and keep track of the biggest ending value for these
  intervals as this value will be the end time of the merged interval.
  time is O(n logn) because of the sorting
'''

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        output = []
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            while i < len(intervals) - 1 and end >= intervals[i + 1][0]: #overlapping
                end = max(end, intervals[i+1][1])
                i += 1
            output.append([start, end])
            i += 1
        return output