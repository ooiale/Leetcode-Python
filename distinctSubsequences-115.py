'''
  we can do a recursive dp algorithm.
  base cases:
    we built the t string: return 1
    with the remaining chars we can't build t: return 0 #optimization
    the current problem has already been solved (is cached): return cache value
    we could cache using just idx, j and not use the curStr var and
    this 4th base case in the code seems unnecessary 
  decision tree:
    include current char if it matches with the car we look for in t
    skip the current char
  time is O(len(s) len(t))
'''

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {} #(curStr, idx) => subsequences
        def dfs(curStr, idx, j):
            if (curStr, idx) in cache:
                return cache[(curStr, idx)]
            if len(t) - len(curStr) > len(s) - idx:
                return 0
            if curStr == t:
                return 1
            if idx >= len(s):
                return 0
            
            possible = 0
            #we can select the current char or not
            if s[idx] == t[j]:
                possible += dfs(curStr + s[idx], idx + 1, j + 1) #select
            possible += dfs(curStr, idx + 1, j) #skip
            cache[(curStr, idx)] = possible
            return cache[(curStr, idx)]
        return dfs('', 0, 0)