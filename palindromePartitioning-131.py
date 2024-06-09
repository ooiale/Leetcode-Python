'''
  we will run a bactracking algorithm
  for every char we do the backtracking, we will check if himself alone
  is a palindrome, and continue the backtracking...
  then on the following iterations we will check if the char itself added
  with the following chars are a palindrome. if so we add it to our partition
  arr and continue the backtracking...
  
'''

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(idx, part):
            if idx == len(s):
                res.append(part[::])
                return
            
            for j in range (idx, len(s)):
                if self.palindrome(s[idx : j + 1]):
                    part.append(s[idx: j + 1])
                    dfs(j + 1, part)
                    part.pop()
                
        dfs(0, [])
        return res
    def palindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True