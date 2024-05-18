'''
  all words have the same prefix so take as a base the first string.
  now iterate through its chars and check if all other strings share the same char 
  in the same position. if not or if your pointer is OoB in the string you are checking, return the prefix found thus far.
  time is O(n m) where n is length of smallest string and m are number of strings
  memory is O(1)
'''

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        i = 0
        while True:
            for w in strs:
                if i >= len(w) or not w[i] == prefix[i]:
                    return prefix[0:i]
            i += 1
