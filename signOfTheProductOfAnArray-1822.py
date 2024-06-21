'''
  cool to talk about number overflow so just look the sign of each number
  instead of doing the actual multiplication to avoid this issue
  too easy anyways
'''

from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for n in nums:
            if n < 0:
                res = -res
            elif n == 0:
                return 0
        return res