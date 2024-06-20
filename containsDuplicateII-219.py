'''
  keep track of seen numbers in a hashMap because we need the values to be the index of the number in the array. since we want i - j <= k it means we always
  want to increase J and since we run through the array in increasing order of index whenever we find a number we update its most recent index in the hashMap
  time is O(n)
'''

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        unique = {}

        for i, v in enumerate(nums):
            if v in unique:
                if (i - unique[v]) <= k:
                    return True
            unique[v] = i
        return False