'''
  we will keep adding the (idx, height) of every height in the list until
  we are unable to extend our current rectangle aka, we want to add an element
  that is smaller than the one on the top of the stack. When this happens, we know
  that the big element in the stack can not be extended to the right any further thus
  it has reached its maximum area. so now, we will pop all elements in the stack 
  that are bigger than the current one and compute the areas formed by them.
  after popping them, we need to store the lowest index of the popped items
  because these bars can still be used at the height of the current height.
  at the end there might be bars that can still be expanded to the right so
  we compute their respective areas as well.
  time is O(n)
'''

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(idx, height)
        res = 0
        i = 0
        while i < len(heights):
            h = heights[i]
            idx = i
            while stack and stack[-1][1] > h:
                idx, val = stack.pop()
                res = max(res, val * (i - idx))
            stack.append((idx, h))
            i += 1
        while stack:
            idx, val = stack.pop()
            res = max(res, val * (i - idx))
        return res