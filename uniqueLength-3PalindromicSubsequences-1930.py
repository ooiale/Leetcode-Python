'''
  get the first and last occurences of a char, the amount of palindromes you can get
  is the number of unique chars in between these two characters
  time is O(n)
  memory is O(n)
'''

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        lastOccurence = {} #char => last idx
        for i, c in enumerate(s):
            lastOccurence[c] = i
        
        res = 0
        visited = set()
        for i, c in enumerate(s):
            lastIdx = lastOccurence[c]
            if i == lastIdx or c in visited:
                continue
            visited.add(c)
            res += len(set(s[i + 1: lastIdx]))
        return res
