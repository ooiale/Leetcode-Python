'''
  lets start from the left and start adding numbers to the left partition.
  at first, leftScore = 0 and rightScore = amount of 1's in entire strnig.
  if we find a 1, decrement rightScore, if we find a 0 increment leftScore
  time is O(n)
'''

class Solution:
    def maxScore(self, s: str) -> int:
        leftScore = 0
        rightScore = 0
        for i in range(len(s)):
            if s[i] == "1":
                rightScore += 1
        
        i = 0
        score = 0
        while i < len(s) - 1:
            if s[i] == "0":
                leftScore += 1
            else:
                rightScore -= 1
            score = max(score, leftScore + rightScore)
            i += 1
        return score