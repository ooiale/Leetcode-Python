'''
  since we are asked not to use division, we will be computing the product
  of the array without self by computing the product of all numbers before and after self. and then the multiplication of these two values is the desired result.
  Time O(n)
'''

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        pre = 1
        aft = 1
        for i in range (len(nums)):
            output[i] = output[i] * pre
            pre = pre * nums[i]
        for j in range (len(nums)):
            output[-1 - j] = output[-1 - j] * aft
            aft = aft * nums[-1 - j]
        return output
            
        