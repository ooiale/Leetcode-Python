'''
  create an array with the start times and the end times and sort them.
  we don't need to worry about losing the info about what (specific) meetings ends at what time
  since we are only worried about any meetings overlapping.
  now we have start two pointers one at start and one at end.
  if start < end it means we are starting a new meeting. 
  once end <= start, it means some meeting that had started has ended
  so we want to know the maximum number of meetings started at one point.
  time is O(n logn) for the sorting
'''


#Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = [], []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        
        i = 0
        j = 0
        count = 0
        output = 0
        while i < len(start):
            if start[i] < end[j]:
                count += 1
                i += 1
                output = max(count, output)
            else:
                count -= 1
                j += 1
        return output