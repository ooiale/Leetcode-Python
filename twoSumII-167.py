'''
  by starting a pointer at the left end of the array and another
  at the very end of it, we can just slide the pointers inwards as
  needed. this is due to the fact the array is sorted.
  time O(n)
  memory O(1)
'''

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1