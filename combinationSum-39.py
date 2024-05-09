'''
  essentially we will perform a recursive DFS to create 
  a possiblity tree. so for each candidate, we will extend the
  branch with all other candidates (itself included).
  to avoid returning permutations of the same combination,
  we will restrict the problem so that once we finish adding
  the same value to its left branch, we won't add it again.
  in other words, once the algorithm stops using a candidate it 
  never uses it again.
  time complexity is O(2^t) = nodes from a tree with height t
  neetcode has a much cleaner way of writing this DFS :/
  https://www.youtube.com/watch?v=GBKI9VSKdGg
  also its possible to refactor this code a little bit
  but I think this way is more clear to see whats happening
'''

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def backtrack(arr, target):
            if sum(arr) == target:
                output.append(arr.copy())
                arr.pop()
                return
            if sum(arr) > target:
                arr.pop()
                return
            if sum(arr) < target:
                idx = 0
                if arr:
                    idx = candidates.index(arr[-1])
                for i in range(idx, len(candidates)):
                    if sum(arr) + candidates[i] <= target:
                        arr.append(candidates[i])
                        backtrack(arr, target)
            if arr:
                arr.pop()

        backtrack([], target)
        return output