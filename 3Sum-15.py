'''
  start by sorting the array.
  now we need to pick 3 numbers for the sum.
  the first one will be fix and will run through each element of the array.
  now to find the other two, we will scan the elements to the right of the 
  first one. with a left and right pointer we can apply the same trick used in 2sum II where we slide the pointers inwards as needed to find the combinations of 2 numbers to add to the reamining value.
  now to avoid getting repeated triples, after we find a valid solution such that  a + b + c = target, we can not repeat the same b (or c) so we will move to the next number != b  which will make the sum invalid so the algorithm proceeds.
  and the other detail is that since we are always scanning all valid b + c so the right of a, we should never perform the algorithm for repeated a's.
  Time is O(n^2)
'''

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == a:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if (a + nums[l] + nums[r] < 0):
                    l += 1
                elif (a + nums[l] + nums[r] > 0):
                    r -= 1
                elif (a + nums[l] + nums[r] == 0):
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
        return res
