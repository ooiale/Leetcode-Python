'''
  we can use a left pointer sliding to the right to compute the sum
  of all numbers on the left half of the array.
  so by computing the sum of the array prior to it we can always know the 
  value of the sum on the right half.
  time is O(n)
'''


from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        i = 0
        while i < len(nums):
            if left == (total - nums[i]) / 2:
                return i
             
            left += nums[i]
            i += 1
        
        return -1