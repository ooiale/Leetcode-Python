'''
  first create an adjacency list for all nodes and edges
  next create a set to track the visited nodes.
  now for every single node that we have not visited yet we will run a DFS
  that will go through all of its neighbors and marking the visit on each of them.
  for every completed DFS we found +1 component.
  to avoid problems with infinite loops, we do not visit the previously visited node and we never visit a node again during the dfs.
  time is O(n + e)
  storage is O(n + e)
'''

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return
            visited.add(node)
            for child in adj[node]:
                if child != prev:
                    dfs(child, node)
        
        output = 0
        for node in adj:
            if node not in visited:
                dfs(node, None)
                output += 1
        
        return output

