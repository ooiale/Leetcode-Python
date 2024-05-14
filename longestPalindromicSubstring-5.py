'''
  instead of checking every single substring which is O(n^3), we will
  go through each character and say that char is the middle of the palindrome,
  then keep expanding its left and right pointers to search for longer palindromes
  since a char is a palindrom with itself, we will do this two times, one considering there is a middle char (aka odd length) and another time with an even length (middle are 2 chars)
  time is O(n^2)
  memory is O(1)
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_l = 0
        res_r = 0
        for i in range(len(s)):
            #odd length, aka middle char is palindrome with itself
            l = i
            r = i    
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) > (res_r - res_l):
                    res_l, res_r = l, r
                r += 1
                l -= 1
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) > (res_r - res_l):
                    res_l, res_r = l, r
                r += 1
                l -= 1
        return s[res_l:res_r + 1]