'''
  at every element in nums we can either pick that number of not pick that number. since we have duplicates, we will sort the nums arr so that when
  we don't want to pick the current number, we will find the next number
  different than that one.
'''

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(idx, subset):
            if idx == len(nums):
                res.append(subset[::])
                return
            
            #lets include the current number
            subset.append(nums[idx])
            dfs(idx + 1, subset)

            #lets not include the current number
            subset.pop()
            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
                idx += 1

            dfs(idx + 1, subset)

        dfs(0, [])
        return res