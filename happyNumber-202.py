'''
  repeat the algorithm until it reaches to 1. to find the loop
  just keep track of the results computed in a set and once a
  value is found in this set a loop was found so return false
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        results = set()
        results.add(n)
        while True:
            SoQ = 0
            for c in str(n):
                SoQ += int(c) ** 2
            n = SoQ
            if SoQ == 1:
                return True
            if SoQ in results:
                return False
            results.add(SoQ)
            
            