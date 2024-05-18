'''
  starting from the end: find the first occurrence of a non empty space.
  now starting from this point, find the first occurrence of an empty space.
  time is O(n)
  memory is O(1)
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = 0
        end = len(s) - 1
        while end - i >= 0 and s[end - i] == " ":
            i += 1
            
        end = end - i
        i = 0
        while end - i >= 0 and s[end - i] != " ":
            i += 1
        return i