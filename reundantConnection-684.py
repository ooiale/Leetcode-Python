'''
  we will use union find algorithm.
  initialize an array where each index points at the root node of that current 'tree'
  everytime we grab an edge, we check if the parents from both nodes from the edge's end are the same. if so thats the loop found. 
  otherwise, we will "connect" these trees. so node n2's parent will now be the parent of n1.
  the find function will just find the parent of each node. 
  time is O(nodes + edges)
'''


from typing import List



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]

        def find(n):
            p = par[n]
            while p != par[p]:
                p = par[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False #loop found
            
            par[p2] = p1
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]