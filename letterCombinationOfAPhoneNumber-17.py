'''
  lets do a backtrack brute force solution to get all 
  possible combinations. Using a hash map eases your life here.
  Worst case scenario, our digit will map to 4 chars, and all mapped
  outputs contain exactly n chars so worst case scenario our algorithm
  runs in time complexity of O(n * 4^n)
'''

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
        res = []

        def dfs(idx, str):
            if idx == len(digits):
                if str:
                    res.append(str)
                return
            mapped = phoneMap[digits[idx]]
            for char in mapped:
                dfs(idx + 1, str + char) 
        
        dfs(0, '')
        return res