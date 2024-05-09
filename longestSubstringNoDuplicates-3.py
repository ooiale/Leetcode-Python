'''
  using sliding window technique, we will keep the pointer l at the start
  of the substring and move r until the end of the string.
  to keep track of duplicates, adding the chars to a set is good since search in it is O(1)
  when str[r] finds a dupicate though, we will need to start moving the l pointer to the right while removing the element string[l] from the set.
  do this until the duplicate element is removed from the set only then proceed to move the right pointer.
  Time is O(n)
  memory is O(n)
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        chars = set()
        while r < len(s):
            if s[r] in chars:
                longest = max(longest, len(chars))
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
            chars.add(s[r])
            r += 1
        return max(longest, len(chars))
