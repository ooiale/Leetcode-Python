'''
  because we need to avoid duplicate combinations, once we decided to skip
  the number x, we will never add it again. so to achieve this we can
  sort the candidates arr.
  now, for each number in the array we can always choose to either select it
  or not select it. if we choose to not select it, we will find the next
  number different from it in the arr (this is why sorting is important)
  now continue this algorithm recursively.
'''

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(idx, arr):
            curSum = sum(arr)
            if curSum == target:
                res.append(arr[::])
                return
            if idx == len(candidates):
                return
            if curSum + candidates[idx] <= target:
                arr.append(candidates[idx])
                dfs(idx + 1, arr)
                arr.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            dfs(idx + 1, arr)
        dfs(0, [])
        return res

