'''
  XOR operation returns 1 if the 2 elements are different and 0 if they are the same
  additionally, n XOR 0 = n so,
  since all elements come in pair but one, once we do the XOR operation on all
  of them, at the end our last operation will be x XOR 0 = x
  time is O(n)
  memory is O(1)
'''

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #neutral element for XOR = 0, because n ^ 0 = n
        res = 0
        for i in nums:
            res = res ^ i
        return res