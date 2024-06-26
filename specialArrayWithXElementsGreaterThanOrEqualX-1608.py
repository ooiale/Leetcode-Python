'''
  our result if it exists must lie within [1, len(nums)]
  first sort the array.
  so we iterate through each number in this range and check if it is
  to keep track of elements greater than or equal to X, we will start
  with all numbers less or equal to than nums[0] because there are len(nums) numbers
  greater than those numbers. once we reach nums[1] we know there is len(nums) - 1
  numbers greater than all the elements ranging from nums[1] to nums[2] (exclusive)
  time is O(n logn)
'''

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # x >= 0
        # x = [1, len(nums)]
        nums.sort()
        x = len(nums)
        prev = 0
        for i in nums:
            for j in range(prev + 1, i + 1):
                if j == x:
                    return j
            x -= 1
            prev = i
        return -1