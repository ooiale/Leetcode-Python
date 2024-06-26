'''
  iterate twice the string:
  first to count the number the char appears
  second to check if any char appears only once. if it does return its index since
  its the first non-repeating character
  time is O(n)
'''

from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1