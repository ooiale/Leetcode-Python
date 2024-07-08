'''
  its the lowest given any combination of k scores.
  so if we sort the array, the idx i and i + k - 1 represent
  the biggest and smallest element out of all combinations with
  those k scores. 
  time is O(n logn)
'''

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        l, r = 0, k - 1
        res = nums[0] - nums[k - 1]

        while r < len(nums):
            res = min(res, nums[l] - nums[r])
            l, r = l + 1, r + 1
        return res