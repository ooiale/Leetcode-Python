'''
  keep a hashMap that keeps track of the idx of the first time a char appears
  in s.
  once we find this char again, we length of the substring in between them is
  the difference of their indices - 1
  time is O(n)
'''

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hashMap = {} #char => idx of first appearance
        res = -1
        for i, c in enumerate(s):
            if c not in hashMap:
                hashMap[c] = i
            else:
                res = max(res, i - hashMap[c] - 1)

        return res