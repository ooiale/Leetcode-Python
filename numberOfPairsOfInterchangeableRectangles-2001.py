'''
  once we find a rectangle with ratio = x, we have 0 pairs.
  once we find the second one we can make 1 pair with the previous one
  once we find the third one we can make 2 pairs, one with each previous one...
  time is O(n)
  memory is O(n)
'''

from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratioCount = {} #width/height ratio => count
        res = 0
        for w, h in rectangles:
            ratio = w/h
            if ratio in ratioCount:
                res += ratioCount[ratio]
                ratioCount[ratio] += 1
            else:
                ratioCount[ratio] = 1
        return res