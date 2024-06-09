'''
  since the end of nums1 is filled with useless values, we might as well start
  filling the array from the end.
  the edge case to watch out for is when the elements in nums1 are greater
  than the elements in nums2 in a way that we push all elements from nums1 to the end of nums1, and we still have elements in nums2 to fill in.
  so at the end of the algorithm we start adding all elements of nums2 in order in nums1
  time is O(n + m)
  memory is O(1)
'''

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = len(nums1) - len(nums2) - 1
        p2 = len(nums2) - 1
        end = len(nums1) - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] <= nums2[p2]:
                nums1[end] = nums2[p2]
                p2 -= 1
            else:
                nums1[end] = nums1[p1]
                p1 -= 1
            end -=1
        while p2 >= 0:
            nums1[p2] = nums2[p2]
            p2 -= 1
        