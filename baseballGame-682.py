'''
  too easy
'''

from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # int => new score
        # + => add score i, i - 1
        # D => doubles score i
        # C => del score i
        scores = []
        total = 0
        for op in operations:
            if op == "+":
                score = scores[-1] + scores[-2]
                scores.append(score)
            elif op == "D":
                score = scores[-1] * 2
                scores.append(score)
            elif op == "C":
                score = scores.pop() * -1
            else:
                score = int(op)
                scores.append(score)
            total += score
        return total