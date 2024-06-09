'''
  DFS where for each element we either include it or not and move
  to the next element. Remember to append a copy of the list to the
  result array.
'''

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(idx, subset):
            if idx == len(nums):
                res.append(subset[::])
                return
            
            #lets select the current number
            subset.append(nums[idx])
            dfs(idx + 1, subset)

            #lets not select the current number
            subset.pop()
            dfs(idx + 1, subset)
        dfs(0, [])       
        return res