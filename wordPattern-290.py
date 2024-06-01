'''
  we need to map each char in pattern to a word in s. we can get the words in s
  by splitting it by space characters.
  if their lengths are different then return false already since there is no bijection.
  now, we need to check if for every char, char maps to word and word maps to char.
  time is O(n + m) where n and m are the number of chars in pattern and s.
  space is O(n + m) for the hash maps
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternHash = {}
        stringHash = {}
        arr = s.split(" ")
        if len(pattern) != len(arr):
            return False
        for i in range(len(pattern)):
            c = pattern[i]
            if arr[i] in stringHash:
                if stringHash[arr[i]] != c:
                    return False
            if c in patternHash:
                if patternHash[c] != arr[i]:
                    return False
            stringHash[arr[i]] = c
            patternHash[c] = arr[i]
        return True 
