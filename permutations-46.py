'''
  backtrack always adding a new number from nums to the permutation
  once the length of the set == len(nums) it means we made one of the 
  permutations. now we backtrack, removing the placed elements and 
  adding the next ones
'''

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def dfs():
            if len(visited) == len(nums):
                res.append(list(visited))
                return
            for i in nums:
                if i not in visited:
                    visited.add(i)
                    dfs()
                    visited.remove(i)
        
        dfs()
        return res