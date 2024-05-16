'''
  using a dynamic programming approach, its very easy to store the largest element to the right of a number by starting the loop through the end.
  and by using a temporary variable to store the current arr[i] value, we can modify the original array in-place for better performance. we start big = -1 just to fulfill the requirement of arr[-1] = -1
  time is O(n)
  memory is O(1)
'''

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        big = -1
        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]
            arr[i] = big
            if tmp > big:
                big = tmp
        return arr