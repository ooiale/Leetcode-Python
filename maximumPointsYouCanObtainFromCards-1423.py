'''
  lets use a sliding window that leaves exactly k elements out of it
  this way we always ensure there are N elements on the left and 
  K - N elements on the right. after sliding our window, we are basically subtracting the previous sum by the element on the right + 1 which is going inside the window and adding to the previous sum the element on the left which is now leaving the window. 
  time is O(k) because we slide the window k times.
  memory is O(1)
'''

from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #make a window that leaves k elements outside of it
        #this way we will end up checking all possible combinations in
        #just O(k) time
        l = 0
        r = len(cardPoints) - k - 1
        output = sum(cardPoints[r + 1::])
        curSum = output
        while r < len(cardPoints) - 1:
            curSum = curSum + cardPoints[l] - cardPoints[r + 1]
            output = max(output, curSum)
            l += 1
            r += 1
        return output