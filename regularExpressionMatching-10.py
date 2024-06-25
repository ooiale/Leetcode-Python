'''
  run a DFS iteratnig through both strings:
  the base case is:
    1- we reached the end of both strings without any issue (i and j are OoB): True
    2- index j is OoB, so we can't match with string s anymore
    3- index i is OoB is not an option because * chars can delete chars from j
  our decision tree are the following:
    1- is the char j + 1 = * ?
      -don't include the char at j and skip to idx j + 2 (skip the char and the star)
      -use the star, a nice way of doing so is by incrementing i to i + 1
    2- char j + 1 is not * but chars i and j match
      -then increment i + 1 and j + 1 
  by including a cache we can reduce the time complexity from 2^n to m * n
  where m and n are the length of each string.
  time is O(m * n)
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {} #(i, j) => False/True 
        def dfs(i, j): 
            #reminder that i OoB is not a problem since chars in J can be 'deleted'
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                #two choices 
                #1- use the star if chars match (move i to i + 1)
                #2- not use the start (move j to j + 2)
                use = match and dfs(i + 1, j)
                notUse = dfs(i, j + 2)
                cache[(i, j)] = use or notUse
                #this return ensures that if there is a * then we will
                #never run anything below it aka run dfs(i + 1,j + 1)
                return cache[(i, j)]
            
            #last choice, chars match and there is no star just move to the next one
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            #if chars don't match and there is no * then just return False
            cache[(i, j)] = False
            return cache[(i, j)]
        return dfs(0, 0)