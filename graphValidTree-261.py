'''
  firstly, create an adjacency list for all nodes and edges.
  now run a DFS through any node. lets start from node 0, 
  our goal is to visit every single node in the tree without 
  visiting any node twice (aka cycle).
  So, to avoid visiting the previous node since its an undirected graph,
  store a variable that points to the previous node. 
  If at some point we visit a node twice return false. and in the end
  make sure to check if we visited all n nodes (tree is connected graph).
  time is O(n + e)
  memory is O(n + e)
'''

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency = {i: [] for i in range(n)}
        for i, j in edges:
            adjacency[j].append(i)
            adjacency[i].append(j)
        
        visited = set()
        
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for child in adjacency[node]:
                if child != prev:
                    if not dfs(child, node):
                        return False
            return True


        return dfs(0, None) and len(visited) == n
            