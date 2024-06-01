'''
  for each interval we will check:
  1) do we insert the new interval before it and it doesnt overlap?
  then insert the new interval and append all the rest of the intervals
  2) is the correct position for the new interval ahead of the ith interval without overlapping?
  then just append this current interval.
  3)else aka does it overlap? then we won't append anything to the array as we are merging 2 overlapping intervals that may overlap with the next intervals as well.
  so the new interval becomes the (min, max) of the interval and new interval.
  time is O(n)
'''

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                #new interval is before the ith interval and doesnt overlap
                output.append(newInterval)
                return output + intervals[i::]
            elif newInterval[0] > intervals[i][1]:
                #new interval is after ith interval and doesnt overlap
                output.append(intervals[i])
            else:
                #interval overlaps so we merge them and dont append anything
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
        output.append(newInterval) #in case the merged interval happens to be the very last interval
        return output
