'''
  we need to find a unique mapping from chars from s => t and
  from t => s.
  if we do so return True.
  if the mapping is not unique return False
  DONT OVERCOMPLICATE AND TRY TO DO THE REPLACEMENT OF CHARS JUST FINDING
  THE UNIQUE MAPPING IS ENOUGH
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS2T, mapT2S = {}, {}

        for c1, c2 in zip(s, t):
            if (c1 in mapS2T and mapS2T[c1] != c2) or (c2 in mapT2S and mapT2S[c2] != c1):
                return False
            mapS2T[c1] = c2
            mapT2S[c2] = c1
        return True