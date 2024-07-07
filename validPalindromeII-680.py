'''
  once you find chars that dont match, check if skipping either of them
  results in palindrome. 
  time is O(n)
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                #we skip either L or R, and skipping one of them needs to be a palindrome
                SL, SR = s[l + 1: r + 1], s[l: r]
                return SL == SL[::-1] or SR == SR[::-1]
            l += 1
            r -= 1
        return True
