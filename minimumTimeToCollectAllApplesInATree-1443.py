'''
  for every neighbor node that has a apple, increase time by 2 and for every
  node that has neighbors with an apple increase time by 2 since we need to visit the node and then come back
  time is O(n) number of nodes
'''

from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for p, c in edges:
            adj[p].append(c)
            adj[c].append(p)
        
        def dfs(prev, node):
            time = 0
            for nei in adj[node]:
                if nei == prev:
                    continue
                neiTime = dfs(node, nei)
                if neiTime or hasApple[nei]:
                    time += 2 + neiTime
            return time
        return dfs(None, 0)

            