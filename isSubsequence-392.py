'''
  all you need to do is try to find all chars from S in their order, in the string T so use a pointer to track the current char you are looking for in S and the char you are scanning in T
  time is O(n)
  memory is O(1)
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cur = 0
        i = 0
        while cur < len(s) and i < len(t):
            if t[i] == s[cur]:
                cur += 1
            i += 1
        if cur == len(s):
            return True
