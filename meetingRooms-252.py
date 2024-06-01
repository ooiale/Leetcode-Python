'''
  sort the array by starting times. this way, we ensure that the meeting i + 1 always start after (or at same time) as the meeting i. This way, we can just check whether meeting i+1 starts after meeting i has ended.
  time is O(nlogn)
'''

from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        prevEnd = 0
        for i in intervals:
            if i.start < prevEnd:
                return False
            prevEnd = i.end
        return True