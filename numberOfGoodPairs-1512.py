'''
  if we have seen the number 1 once, when we find another number 1, we can make
  1 pair.
  If we have seen the number 1 twice and we find another number 1, we can make
  2 pairs.
  so keep track of the amount of times you have seen each number in a hashMap and iterate through the array.
  time is O(n)
  memory is O(n)
'''

from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = {}
        output = 0
        for n in nums:
            if n in hashMap:
                output += hashMap[n]
            hashMap[n] = 1 + hashMap.get(n, 0)
        return output
        