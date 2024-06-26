'''
  create a hashSet with the numbers of nums1,
  then iterate through nums2 and add the numbers that are also in the set
  to avoid duplicates, remove the number from the set once you have appended it to the res arr.
  time is O(n)
'''

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        res = []
        for i in nums1:
            set1.add(i)
        for i in nums2:
            if i in set1:
                res.append(i)
                set1.remove(i)
        return res