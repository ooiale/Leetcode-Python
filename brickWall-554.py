'''
  the number of bricks we cut is the height of the brick wall - the number of gaps at
  a certain spot. This is very efficient because in the case we have a wall:
  [100], [100] we would only check that one spot, the gap.
  so basically we iterate through all bricks and count the number of gaps at each spot
  we find a gap. this can be easily done with a hashMap
  the time complexity and memory complexity is O( number of bricks )
'''

from collections import defaultdict
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps = defaultdict(int) #gap => no of cuts

        for i in range(len(wall)):
            aux = 0
            for j in range(0, len(wall[i]) - 1):
                aux += wall[i][j]
                gaps[aux] += 1
        
        res = float("inf")
        for key in gaps:
            res = min(res, len(wall) - gaps[key])
        if res == float("inf"):
            return len(wall)
        return res