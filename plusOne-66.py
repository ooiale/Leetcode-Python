'''
  dont forget about the increments...
  if there is increment after looping through all numbers we just need
  to add a leading 1.
  time is O(n)
'''

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        increment = 0
        for i in range(len(digits) - 1, -1, -1):
            increment = (digits[i] + 1) // 10
            digits[i] = (digits[i] + 1) % 10
            if increment == 0:
                break
        if increment:
            digits = [1] + digits
        return digits