'''
  count the amount of times each letter in balloon shows up
  time is O(n)
  memory is O(5) = O(1)
'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash = {c: 0 for c in 'balon'}
        for c in text:
            if c in hash:
                hash[c] += 1
        
        res = float('inf')
        for key, value in hash.items():
            if key in ['b', 'a', 'n']:
                res = min(res, value)
            else:
                res = min(res, value//2)
        return res