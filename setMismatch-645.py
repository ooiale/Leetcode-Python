'''
  using a hashSet we can keep track of the values visited and visited twice.
  time is O(n)
  memory is O(n)
  There is an elegant but harder solution to achieve an in-place algorithm
  abusing the fact that we can map the values in the array to an index 
  by doing i = n -1
'''

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing = 0
        duplicate = 0

        fullSet = set([i for i in range(1, len(nums) + 1)])

        for n in nums:
            if n in fullSet:
                fullSet.remove(n)
            else:
                duplicate = n
        for i in fullSet:
            missing = i
        return [duplicate, missing]