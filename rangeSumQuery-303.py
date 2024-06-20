'''
  create a prefix sum array: for each index in the array, it contains the
  sum of all numbers up to this point.
  now finding the sumRange is O(1) since we want the sum of all elements
  up to idx right minus the um of all elements that comes before left index
  time is O(n) for the constructor 
  time is O(1) for the method
'''

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        sumSoFar = 0
        self.prefix = []
        for i in nums:
            sumSoFar += i
            self.prefix.append(sumSoFar)
    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.prefix[right] - self.prefix[left - 1]
        return self.prefix[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)