'''
  use a set to avoid duplications and search/removal/append are all O(1)
'''

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        visited = set()
        ans1 = set()
        ans2 = set()
        for i in nums1:
            visited.add(i)
            ans1.add(i)
        for i in nums2:
            if i not in visited:
                ans2.add(i)
            if i in ans1:
                ans1.remove(i)
        return [list(ans1), list(ans2)]