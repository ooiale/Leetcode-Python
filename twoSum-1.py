'''
  create a hash map and iterate through the array once. 
  at each element, store target - element as the hash key
  and the value the index.
  this way, we can always search if the current value is in the hash map
  since the keys in the hash map points to the index of the element complementary to the one we are currently searching
  Time O(n)
  memory O(n)
'''

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, v in enumerate(nums):
            if (v in hash):
                return [hash[v], i]
            hash[target - v] = i 
            