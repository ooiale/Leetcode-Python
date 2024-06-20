'''
  so for every element in the array we can either select it positive
  or negative. so we can make a backtracking algorithm for that.
  to improve efficience we can include a cache that will tell us
  how many possible ways to achieve sum of target based on the 
  idx and curSum at the current iteration.
'''

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {} #(idx, curSum) => number of ways to add to target from there
        def dfs(curSum, idx):
            if (idx, curSum) in cache:
                return cache[(idx, curSum)]
            if idx == len(nums): 
                if curSum == target:
                    return 1
                return 0
            
            #we can add or subtract the visited number
            cache[(idx, curSum)] = dfs(curSum + nums[idx], idx + 1) + dfs(curSum - nums[idx], idx + 1)
            return cache[(idx, curSum)]
        
        return dfs(0, 0)
            