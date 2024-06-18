'''
  this can be seen as a graph problem of finding the tree with minimum cost (MST)
  which can be solved with Prim's algorithm. 
  basically we will create an weighted adjacency list with every single edge possible in this graph, and then we apply djisktra algorithm to find the minimum cost path.
  so basically, starting from any node, add all its neighbors to a minHeap,
  then we peform a BFS by popping from the heap as opposed to the usual queue from normal BFS.
  keep track of the visited nodes so that we don't generate any cycles.
  once the graph has exactly n-1 edges then it is a tree and we can stop
  the algorithm
  time is O(E log(E)) where E is the number of edges = n^2 with n = number of nodes
'''


from collections import defaultdict
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def getDist(x1, x2, y1, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        
        adj = defaultdict(list) #(i, j) => list [w, i*, j*]

        for x1, y1 in points:
            for x2, y2 in points:
                if (x1, y1) != (x2, y2):
                    adj[(x1, y1)].append([getDist(x1,x2,y1,y2), x2, y2])
        
        visited = set()
        minHeap = [(0, x1, y1)]
        res = 0
        while len(visited) < len(points):
            c1, x1, y1 = heapq.heappop(minHeap)
            if (x1, y1) in visited:
                continue
            res += c1
            visited.add((x1, y1))
            for c2, x2, y2 in adj[(x1, y1)]:
                if (x2, y2) in visited:
                    continue
                heapq.heappush(minHeap, (c2, x2, y2))
        
        return res