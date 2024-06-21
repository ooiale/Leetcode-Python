'''
  backtracking with cache.
  for each iteration you can either include the char in s1 or the char in s2.
  at (idx1, idx2) we are interested if its possible to make s3 in any possible way
  so if cache[(idx1, idx2)] = true if the backtracking including either c1 or c2 works.
  time is O(len(s1) * len(s2))
'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        cache = {} 
        def dfs(idx1, idx2):
            if idx1 + idx2 == len(s3):
                return True
            if (idx1, idx2) in cache:
                return cache[(idx1, idx2)]
            
            idx3 = idx1 + idx2
            opt1, opt2 = False, False
            if idx1 < len(s1) and s1[idx1] == s3[idx3]:
                opt1 = dfs(idx1 + 1, idx2)
            if idx2 < len(s2) and s2[idx2] == s3[idx3]:
                opt2 =  dfs(idx1, idx2 + 1)
            cache[(idx1, idx2)] = opt1 or opt2
            return cache[(idx1, idx2)]
        return dfs(0, 0)