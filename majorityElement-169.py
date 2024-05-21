'''
  this solution with O(1) memory and O(n) time is very tricky.
  #MAJORITY ELEMENT MEANS THERE IS AT LEAST N // 2 + 1 ELEMENTS IN THE
  ARRAY where n is the length of it. so, we can just keep track of one element
  and start incrementing its count whenever we find a pair or decrement once we 
  find a different element. once the count = 0, it means we have found an equal amount of a specific number and numbers that are not that specific one. 
  therefore, the next element we find we will say its the majority one.
  because the majority one appears N // 2 + 1 times it will always have at least count = 1 at the end.
'''

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n, c = nums[0], 0
        #if I find n, c += 1 else, c -= 1
        #if c = 0 we swap what n is with the current visited char
        for i in nums:
            if c == 0:
                n = i
            if i == n:
                c += 1
            else:
                c -= 1
        return n