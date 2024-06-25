'''
  we can simulate the situation at each 'second'
  simulate the situation going from left to right using a queue.
  since only dominoes "R" or "L" require an action just append these values to
  the queue. just watch out when you have a "R" domino and 2 elements ahead there is a "L" domino because in this case we know these 2 dominoes won't do anything so go ahead and .pop() this next "L"
  time is O(n)
'''

from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        queue = deque([])
        for i in range(len(dominoes)):
            if dominoes[i] in ["R", "L"]:
                queue.append(i)

        while queue:
            i = queue.popleft()
            if dominoes[i] == "R":
                if i + 1 < len(dominoes) and dominoes[i + 1] == ".":
                    if i + 2 < len(dominoes) and dominoes[i + 2] == "L":                        
                        queue.popleft()
                        continue
                    dominoes[i + 1] = "R"
                    queue.append(i + 1)
            elif dominoes[i] == "L":
                if i - 1 >= 0 and dominoes[i - 1] == ".":
                    dominoes[i - 1] = "L"
                    queue.append(i - 1)

        return ''.join(dominoes)