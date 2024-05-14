'''
  same algorithm as lc 5, but instead of storing the largest palindrome
  we just count the times we find a palindrome.
  time is O(n^2)
  storage is O(1)
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                output += 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                output += 1
                l -= 1
                r += 1
        return output