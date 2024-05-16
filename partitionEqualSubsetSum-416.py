'''
  first of all, the problem can only have a solution if the sum of nums is even.
  now, since we know the sum of all numbers in the list is Target, if at some point we find a subset with sum N, we know that there must exist a remaining subset that sums up to Target - N.
  Therefore, the algorithm will search if at some point any subset that adds up to Target//2. 
  the trick for this is to use a set initialized with 0. loop through all numbers and add to this set all values of the set added to the current number.
  time is O(n * target) since we loop through all numbers once and for each number we loop through all numbers in the set
  memory is O(target) since we store values up to target in the set
'''

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        possibleSums = set([0])

        for n in nums:
            tempSet = set()
            for j in possibleSums:
                if target in tempSet:
                    return True
                if j+n <= target:
                    tempSet.add(j + n)
                tempSet.add(j)
            possibleSums = tempSet
        return False