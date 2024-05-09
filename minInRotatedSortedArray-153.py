'''
  lets use binary search to find where the minimum is.
  so get the middle index and check. is it greater than the right most element?
  if so it means the left side are all bigger than the right side. (remember the array is sorted on the left side and on the right side)
  otherwise, the left side is the one that contains the minimum.
  perform this until one element is left (aka l == r)
  time is O(log(n))
'''

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            m = (l+r)//2
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]

             