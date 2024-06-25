'''
  iterate through array: once you find a matching char try to see if you can 
  find the needle word. if the matched char did not result in the needle word.
  return to the index we were at and continue the iteration. the index J is
  useful to "reset" this search.
  on average this should be a O(n) time. worst case it is a O(n * m) 
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                j += 1
            else:
                i = i - j
                j = 0
            i += 1
            if j == len(needle):
                return i - j
        return -1